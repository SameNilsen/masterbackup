import time

import subprocess as sp
import sys
from threading import Timer
import datetime
import argparse
import os

running = True

def get_total_gpu_memory():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=memory.total --format=csv"
    try:
        memory_total_info = output_to_list(sp.check_output(COMMAND.split(),stderr=sp.STDOUT))[1:]
    except sp.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    memory_total_values = [int(x.split()[0]) for i, x in enumerate(memory_total_info)]
    # print(memory_total_values)
    return memory_total_values

def get_gpu_utilization():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=utilization.gpu --format=csv"
    try:
        gpu_utilization_info = output_to_list(sp.check_output(COMMAND.split(),stderr=sp.STDOUT))[1:]
    except sp.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    gpu_utilization_values = [int(x.split()[0]) for i, x in enumerate(gpu_utilization_info)]
    # print(gpu_utilization_values)
    return gpu_utilization_values

def get_power_draw():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=power.draw --format=csv"
    try:
        power_draw_info = output_to_list(sp.check_output(COMMAND.split(),stderr=sp.STDOUT))[1:]
    except sp.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    power_draw_values = [float(x.split()[0]) for i, x in enumerate(power_draw_info)]
    # print(power_draw_values)
    return power_draw_values

def get_gpu_memory():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=memory.used --format=csv"
    try:
        memory_use_info = output_to_list(sp.check_output(COMMAND.split(),stderr=sp.STDOUT))[1:]
    except sp.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    memory_use_values = [int(x.split()[0]) for i, x in enumerate(memory_use_info)]
    # print(memory_use_values)
    return memory_use_values


def print_gpu_memory_every_5secs():
    """
        This function calls itself every 5 secs and print the gpu_memory.
    """
    if running is False:
        return
    print("starting: print_gpu_memory_every_5secs")
    Timer(5.0, print_gpu_memory_every_5secs).start()
    print(get_gpu_memory())


def compute_avg_values(gpu_usage_values_total, gpu_utilization_values_total, power_draw_values_total):
    len_usage, total_usage = 0, 0
    for i in range(len(gpu_usage_values_total)):
        # print(gpu_usage_values_total[i])
        for o in range(len(gpu_usage_values_total[i])):
            # print(gpu_usage_values_total[i][o], gpu_usage_values_total[i][o][0])
            if gpu_usage_values_total[i][o][0] > 5000:
                total_usage += gpu_usage_values_total[i][o][0]
                len_usage += 1
    print(total_usage, len_usage, total_usage/len_usage)

    len_util, total_util = 0, 0
    for i in range(len(gpu_utilization_values_total)):
        # print(gpu_utilization_values_total[i])
        for o in range(len(gpu_utilization_values_total[i])):
            # print(gpu_utilization_values_total[i][o], gpu_utilization_values_total[i][o][0])
            if gpu_utilization_values_total[i][o][0] > 5:
                total_util += gpu_utilization_values_total[i][o][0]
                len_util += 1
    print(total_util, len_util, total_util/len_util)

    len_power, total_power = 0, 0
    for i in range(len(power_draw_values_total)):
        # print(power_draw_values_total[i])
        for o in range(len(power_draw_values_total[i])):
            # print(power_draw_values_total[i][o], power_draw_values_total[i][o][0])
            if power_draw_values_total[i][o][0] > 79:
                total_power += power_draw_values_total[i][o][0]
                len_power += 1
    print(total_power, len_power, total_power/len_power)

    return total_usage/len_usage, total_util/len_util, total_power/len_power



def stubAskLLM(query, args):
    print("Asking LLM...")
    if (args.inference_provider == "vllm"):
         result = vLLM_configurable.callvLLM(query, llm, samplingparams)
    elif (args.model == "normistral11b_thinking" and args.inference_provider == "transformers"):
         result = normistral11b_configurable.askLLM(query)
    elif ((args.model == "gpt_oss_20b" or args.model == "gpt_oss_120b") and args.inference_provider == "transformers"):
         result = gpt_oss_configurable.askLLM(tokenizer, model, query)
    
    return result

listOfPrompts = {
        "prompt1": "What is 2+2?", 
        "prompt2": "What is the capital of France?", 
        "prompt3": "What is the meaning of life?", 
        "prompt4": "How many continents are there on Earth?", 
        "prompt5": "How are you doing today?",
        "prompt6": "Which city is the Eiffel Tower located in?", 
        "prompt7": "How many legs does a spider have?", 
        "prompt8": "What is the largest mammal?", 
        "prompt9": "What is the chemical symbol for water?", 
        "prompt10": "Who is the current president of the United States?"}

listOfPrompts2 = {
    "prompt11": "What is 5+3?",
    "prompt12": "What is the capital of Spain?",
    "prompt13": "What color is the sky on a clear day?",
    "prompt14": "How many days are there in a week?",
    "prompt15": "How do you say hello in English?",
    "prompt16": "Which planet is known as the Red Planet?",
    "prompt17": "How many wheels does a bicycle have?",
    "prompt18": "What is the smallest prime number?",
    "prompt19": "What do bees produce?",
    "prompt20": "Who wrote the play Romeo and Juliet?"
}

def makeRequest(promptnr, query, timer_log, response_log, args):
    print(f"MakeRequest called with promptnr {promptnr} and query {query}")
    start = time.perf_counter()
    starttime = str(datetime.datetime.now())
    #### CALL GET GPU USAGE EVERY 3 SECONDS IN A SEPARATE THREAD, LOG TO FILE.
    gpu_usage_values = []
    gpu_utilization_values = []
    power_draw_values = []
    with ThreadPoolExecutor(max_workers=5) as exe:
        future = exe.submit(stubAskLLM, query, args)
        while not future.done():
            print(promptnr+": Waiting for LLM response...")
            time.sleep(1)
            gpu_usage_values.append(get_gpu_memory())
            gpu_utilization_values.append(get_gpu_utilization())
            power_draw_values.append(get_power_draw())
    result = future.result()
    endtime = str(datetime.datetime.now())
    
    with open(response_log, "a") as f:
        f.write("\n"+promptnr + " of the 10 requests: \nQuery: " + query + "\nResponse: " + result + "\n")
    end = time.perf_counter()
    with open(timer_log, "a") as f:
        f.write("\n"+promptnr + " of the 10 requests: \nTime taken for comparisons: " + str(end - start) + " seconds.\n Starttime: " + starttime + " Endtime: " + endtime + "\nWith GPU memory usage values (MiB): " + str(gpu_usage_values) + "\nGPU utilization values (%): " + str(gpu_utilization_values) + "\nPower draw values (W): " + str(power_draw_values) + "\n")
    return gpu_usage_values, gpu_utilization_values, power_draw_values

def vLLMsimultaneousRequests(args, base_path):
    timer_log = base_path + "comparisons_vllm_simultaneous.txt"
    response_log = base_path + "comparisons_vllm_simultaneous_output_log.txt"
    initial_loaded_gpu_mem = get_gpu_memory()
    print("Get initial GPU memory: ", initial_loaded_gpu_mem)
    with open(timer_log, "w") as f:
        f.write("--- Starting comparisons --- \n")
        f.write("Initial GPU memory loaded: " + str(initial_loaded_gpu_mem) + " MiB\nOf total GPU memory: " + str(get_total_gpu_memory()) + " MiB\n")
    
    with open(response_log, "w") as f:
        f.write("--- Starting logging responses --- \n")

    print("Starting comparisons.")
    print("Doing 10 requests...")
    startTotal = time.perf_counter()

    newList=[]
    for key, value in listOfPrompts.items():
        newList.append(value)

    gpu_usage_values = []
    gpu_utilization_values = []
    power_draw_values = []
    with ThreadPoolExecutor(max_workers=5) as exe:
        future = exe.submit(vLLM_configurable.makeSimultaneousvLLMRequest, newList, llm, samplingparams)
        while not future.done():
            print("Waiting for LLM response...")
            time.sleep(1)
            gpu_usage_values.append(get_gpu_memory())
            gpu_utilization_values.append(get_gpu_utilization())
            power_draw_values.append(get_power_draw())
    responses = future.result()
    # responses = vLLM_configurable.makeSimultaneousvLLMRequest(newList, llm, samplingparams)
    endTotal = time.perf_counter()
    avg_gpu_usage_values, avg_gpu_utilization_values, avg_power_draw_values = compute_avg_values([gpu_usage_values], [gpu_utilization_values], [power_draw_values])

    with open(timer_log, "a") as f:
            f.write("\nIn total for 10 requests: Time taken for comparisons: " + str(endTotal - startTotal) + " seconds.\nWith GPU memory usage values (MiB): " + str(gpu_usage_values) + "\nGPU utilization values (%): " + str(gpu_utilization_values) + "\nPower draw values (W): " + str(power_draw_values) + "\nWith avg GPU memory usage values (MiB): " + str(avg_gpu_usage_values) + "\navg GPU utilization values (%): " + str(avg_gpu_utilization_values) + "\navg Power draw values (W): " + str(avg_power_draw_values) + "\n")
    with open(response_log, "a") as f:
        for output in responses:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            f.write("\n\nQuery: " + prompt + "\nResponse: " + generated_text + "\n")

def comparisonsNoThreading(args, base_path):
    timer_log = base_path + "comparisons.txt"
    response_log = base_path + "comparisons_output_log.txt"
    initial_loaded_gpu_mem = get_gpu_memory()
    print("Get initial GPU memory: ", initial_loaded_gpu_mem)
    with open(timer_log, "w") as f:
        f.write("--- Starting comparisons --- \n")
        f.write("Initial GPU memory loaded: " + str(initial_loaded_gpu_mem) + " MiB\nOf total GPU memory: " + str(get_total_gpu_memory()) + " MiB\n")
    
    with open(response_log, "w") as f:
        f.write("--- Starting logging responses --- \n")

    print("Starting comparisons.")

    print("1 request, baseline...")
    makeRequest("promptBaseline", "Which city is the Eiffel Tower located in?", timer_log, response_log, args)

    print("Doing 10 requests...")
    gpu_usage_values_total, gpu_utilization_values_total, power_draw_values_total = [], [], []
    startTotal = time.perf_counter()
    for prompt in listOfPrompts.keys():
        query = listOfPrompts[prompt]
        print(f"Handling {prompt} with query {query}...")
        gpu_usage_values, gpu_utilization_values, power_draw_values = makeRequest(prompt, query, timer_log, response_log, args)
        gpu_usage_values_total.append(gpu_usage_values)
        gpu_utilization_values_total.append(gpu_utilization_values)
        power_draw_values_total.append(power_draw_values)
    endTotal = time.perf_counter()
    avg_gpu_usage_values, avg_gpu_utilization_values, avg_power_draw_values = compute_avg_values(gpu_usage_values_total, gpu_utilization_values_total, power_draw_values_total)
    with open(timer_log, "a") as f:
            f.write("\nIn total for 10 requests: Time taken for comparisons: " + str(endTotal - startTotal) + " seconds.\nWith avg GPU memory usage values (MiB): " + str(avg_gpu_usage_values) + "\navg GPU utilization values (%): " + str(avg_gpu_utilization_values) + "\navg Power draw values (W): " + str(avg_power_draw_values) + "\n")


from concurrent.futures import ThreadPoolExecutor

def cube(x):
    print("in cube")
    return x*x*x
def comparisonsThreading(args, base_path):
    timer_log = base_path + "comparisons_threading.txt"
    response_log = base_path + "comparisons_output_log_threading.txt"
    print("Doing comparisons with threading...")
    initial_loaded_gpu_mem = get_gpu_memory()
    print("Get initial GPU memory: ", initial_loaded_gpu_mem)
    with ThreadPoolExecutor(max_workers=10) as exe:
        with open(timer_log, "w") as f:
            f.write("--- Starting comparisons --- \n")
            f.write("Initial GPU memory loaded: " + str(initial_loaded_gpu_mem) + " MiB\nOf total GPU memory: " + str(get_total_gpu_memory()) + " MiB\n")
        
        with open(response_log, "w") as f:
            f.write("--- Starting logging responses --- \n")

        print("Starting comparisons.")

        print("1 request, baseline...")
        makeRequest("promptBaseline", "Which city is the Eiffel Tower located in?", timer_log, response_log, args)

        print("Doing 10 requests...")
        gpu_usage_values_total, gpu_utilization_values_total, power_draw_values_total = [], [], []
        startTotal = time.perf_counter()
        print("starting threads")
        futures = []
        for prompt in listOfPrompts.keys():
            query = listOfPrompts[prompt]
            print(f"Handling {prompt} with query {query}...")
            future = exe.submit(makeRequest, prompt, query, timer_log, response_log, args)
            futures.append(future)
            # makeRequest(prompt, query, timer_log, response_log)
        for future in futures:
            gpu_usage_values, gpu_utilization_values, power_draw_values = future.result()
            gpu_usage_values_total.append(gpu_usage_values)
            gpu_utilization_values_total.append(gpu_utilization_values)
            power_draw_values_total.append(power_draw_values)
        exe.shutdown(wait=True)
        endTotal = time.perf_counter()
        avg_gpu_usage_values, avg_gpu_utilization_values, avg_power_draw_values = compute_avg_values(gpu_usage_values_total, gpu_utilization_values_total, power_draw_values_total)
        print("All threads completed.")
        with open(timer_log, "a") as f:
                f.write("\nIn total for 10 requests: Time taken for comparisons: " + str(endTotal - startTotal) + " seconds.\nWith avg GPU memory usage values (MiB): " + str(avg_gpu_usage_values) + "\navg GPU utilization values (%): " + str(avg_gpu_utilization_values) + "\navg Power draw values (W): " + str(avg_power_draw_values) + "\n")
            
prompt_big = """
You are an analysis expert tasked with answering questions using your knowledge, a curated playbook of strategies and insights and a reflection that goes over the diagnosis of all previous mistakes made while answering the question.

**Instructions:**
- Read the playbook carefully and apply relevant strategies, formulas, and insights
- Pay attention to common mistakes listed in the playbook and avoid them
- Show your reasoning step-by-step
- Be concise but thorough in your analysis
- If the playbook contains relevant code snippets or formulas, use them appropriately
- Double-check your calculations and logic before providing the final answer

Your output should be a json object, which contains the following fields:
- reasoning: your chain of thought / reasoning / thinking process, detailed analysis and calculations
- bullet_ids: each line in the playbook has a bullet_id. all bulletpoints in the playbook that's relevant, helpful for you to answer this question, you should include their bullet_id in this list
- final_answer: your concise final answer


**Playbook:**
## STRATEGIES & INSIGHTS

## FORMULAS & CALCULATIONS

## CODE SNIPPETS & TEMPLATES

## COMMON MISTAKES TO AVOID

## PROBLEM-SOLVING HEURISTICS

## CONTEXT CLUES & INDICATORS

## OTHERS

**Reflection:**
(empty)

**Question:**
You are XBRL expert.  Here is a list of US GAAP tags options: ,OperatingLeasesRentExpenseNet,MinorityInterestOwnershipPercentageByParent,ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue,DerivativeNotionalAmount,PreferredStockDividendRatePercentage,GuaranteeObligationsMaximumExposure,LossContingencyEstimateOfPossibleLoss,OperatingLeaseRightOfUseAsset,NumberOfOperatingSegments,PaymentsToAcquireBusinessesNetOfCashAcquired,DebtInstrumentBasisSpreadOnVariableRate1,InterestExpense,ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber,CommonStockSharesOutstanding,StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1,LineOfCreditFacilityInterestRateAtPeriodEnd,ContractWithCustomerLiabilityRevenueRecognized,AmortizationOfIntangibleAssets,ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1,DebtInstrumentRedemptionPricePercentage,RepaymentsOfDebt,DisposalGroupIncludingDiscontinuedOperationConsideration,LineOfCreditFacilityRemainingBorrowingCapacity,BusinessCombinationAcquisitionRelatedCosts,LesseeOperatingLeaseRenewalTerm,TreasuryStockValueAcquiredCostMethod,PreferredStockSharesAuthorized,RelatedPartyTransactionExpensesFromTransactionsWithRelatedParty,ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue,UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate,SaleOfStockNumberOfSharesIssuedInTransaction,OperatingLeaseWeightedAverageRemainingLeaseTerm1,StockRepurchaseProgramAuthorizedAmount1,SupplementalInformationForPropertyCasualtyInsuranceUnderwritersPriorYearClaimsAndClaimsAdjustmentExpense,RelatedPartyTransactionAmountsOfTransaction,CommonStockDividendsPerShareDeclared,IncomeLossFromEquityMethodInvestments,DebtInstrumentMaturityDate,LettersOfCreditOutstandingAmount,AllocatedShareBasedCompensationExpense,EffectiveIncomeTaxRateContinuingOperations,ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized,ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant,ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross,ConcentrationRiskPercentage1,OperatingLeasePayments,LongTermDebt,RestructuringCharges,CommonStockParOrStatedValuePerShare,DebtInstrumentConvertibleConversionPrice1,Revenues,DeferredFinanceCostsGross,EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate,DefinedBenefitPlanContributionsByEmployer,GoodwillImpairmentLoss,LossContingencyPendingClaimsNumber,OperatingLeaseLiability,LineOfCreditFacilityMaximumBorrowingCapacity,OperatingLeaseExpense,DerivativeFixedInterestRate,LineOfCreditFacilityCommitmentFeePercentage,CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption,SharebasedCompensationArrangementBySharebasedPaymentAwardAwardVestingRightsPercentage,DebtWeightedAverageInterestRate,PaymentsToAcquireBusinessesGross,DebtInstrumentCarryingAmount,BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles,RevenueFromContractWithCustomerExcludingAssessedTax,PublicUtilitiesRequestedRateIncreaseDecreaseAmount,ContractWithCustomerLiability,DebtInstrumentTerm,DebtInstrumentFairValue,RevenueFromContractWithCustomerIncludingAssessedTax,RevenueFromRelatedParties,DebtInstrumentInterestRateEffectivePercentage,GainsLossesOnExtinguishmentOfDebt,EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedShareBasedAwardsOtherThanOptions,DebtInstrumentUnamortizedDiscount,LineOfCreditFacilityCurrentBorrowingCapacity,CashAndCashEquivalentsFairValueDisclosure,LesseeOperatingLeaseTermOfContract,RestructuringAndRelatedCostExpectedCost1,DefinedContributionPlanCostRecognized,OperatingLeaseCost,LossContingencyDamagesSoughtValue,ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodWeightedAverageGrantDateFairValue,ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod,EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1,EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized,FiniteLivedIntangibleAssetUsefulLife,Depreciation,AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife,DeferredFinanceCostsNet,DebtInstrumentInterestRateStatedPercentage,Goodwill,CommonStockCapitalSharesReservedForFutureIssuance,LongTermDebtFairValue,OperatingLossCarryforwards,InterestExpenseDebt,UnrecognizedTaxBenefits,BusinessCombinationContingentConsiderationLiability,TreasuryStockAcquiredAverageCostPerShare,ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1,SharebasedCompensationArrangementBySharebasedPaymentAwardExpirationPeriod,NumberOfRealEstateProperties,TreasuryStockSharesAcquired,AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount,CommonStockSharesAuthorized,SharePrice,DebtInstrumentFaceAmount,AmortizationOfFinancingCosts,BusinessCombinationConsiderationTransferred1,LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage,StockRepurchasedDuringPeriodShares,ProceedsFromIssuanceOfCommonStock,StockIssuedDuringPeriodSharesNewIssues,AccrualForEnvironmentalLossContingencies,BusinessAcquisitionPercentageOfVotingInterestsAcquired,LossContingencyAccrualAtCarryingValue,OperatingLeaseWeightedAverageDiscountRatePercent,ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue,BusinessAcquisitionEquityInterestsIssuedOrIssuableNumberOfSharesIssued,CapitalizedContractCostAmortization,NumberOfReportableSegments,AssetImpairmentCharges,RevenueRemainingPerformanceObligation,EquityMethodInvestmentOwnershipPercentage,MinorityInterestOwnershipPercentageByNoncontrollingOwners,AreaOfRealEstateProperty,StockRepurchasedAndRetiredDuringPeriodShares,LineOfCredit,BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill,IncomeTaxExpenseBenefit,PropertyPlantAndEquipmentUsefulLife,LeaseAndRentalExpense,ShareBasedCompensation,EquityMethodInvestments,SaleOfStockPricePerShare,EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense. Answer the following 4 independent questions by providing only  4 US GAAP tags answers in the order of the questions. Each answer must be saperated by a comma (,).  Provide nothing else. 
1. What is best tag for entity "13,699,549" in sentence: "On August 1 , 2018 , CVR Energy completed an exchange offer whereby CVR Refining 's public unitholders tendered a total of 21,625,106 common units of CVR Refining in exchange for 13,699,549 shares of CVR Energy common stock .?"
2. What is best tag for entity "99" in sentence: "During 2016 , CVR Partners acquired a nitrogen fertilizer business for total purchase price consideration which included the issuance of common units of CVR Partners with a fair value of $ 335 million , cash paid of $ 99 million and debt assumed with a fair value of $ 368 million .?"
3. What is best tag for entity "162" in sentence: "Precision Tune and American Driveline were acquired in 2017 for an aggregate purchase price of $ 162 million .?"
4. What is best tag for entity "1.2" in sentence: "Pep Boys was acquired in 2016 for aggregate consideration of approximately $ 1.2 billion .?"
Output US GAAP tags:

**Context:**


**Answer in this exact JSON format:**
{
  "reasoning": "[Your chain of thought / reasoning / thinking process, detailed analysis and calculations]",  
  "bullet_ids": ["calc-00001", "fin-00002"],  
  "final_answer": "[Your concise final answer here]"
}

---
"""

def xbrlComparisons(args, base_path):
    print("Doing comparisons with xbrl...")
    timer_log = base_path + "comparisons_xbrl.txt"
    response_log = base_path + "comparisons_xbrl_output_log.txt"
    initial_loaded_gpu_mem = get_gpu_memory()
    print("Get initial GPU memory: ", initial_loaded_gpu_mem)
    with open(timer_log, "w") as f:
        f.write("--- Starting comparisons --- \n")
        f.write("Initial GPU memory loaded: " + str(initial_loaded_gpu_mem) + " MiB\nOf total GPU memory: " + str(get_total_gpu_memory()) + " MiB\n")
    
    with open(response_log, "w") as f:
        f.write("--- Starting logging responses --- \n")

    print("Starting comparisons.")
    gpu_usage_values_total, gpu_utilization_values_total, power_draw_values_total = [], [], []
    startTotal = time.perf_counter()
    gpu_usage_values, gpu_utilization_values, power_draw_values = makeRequest("prompt1", prompt_big, timer_log, response_log, args)
    endTotal = time.perf_counter()
    gpu_usage_values_total.append(gpu_usage_values)
    gpu_utilization_values_total.append(gpu_utilization_values)
    power_draw_values_total.append(power_draw_values)
    avg_gpu_usage_values, avg_gpu_utilization_values, avg_power_draw_values = compute_avg_values(gpu_usage_values_total, gpu_utilization_values_total, power_draw_values_total)

    with open(timer_log, "a") as f:
            f.write("\nIn total for 1 requests: Time taken for comparisons: " + str(endTotal - startTotal) + " seconds.\n With avg GPU memory usage values (MiB): " + str(avg_gpu_usage_values) + "\navg GPU utilization values (%): " + str(avg_gpu_utilization_values) + "\navg Power draw values (W): " + str(avg_power_draw_values) + "\n")


def initPrev():
    print(f"Total GPU memory: {get_total_gpu_memory()}")

    print("Setup LLM...")
    # import localLLMqwen
    # import localLLM
    # localLLM.setupLLM()
    import normistral_vllm_2
    if __name__ == "__main__":
        llm = normistral_vllm_2.load()
        samplingparams = normistral_vllm_2.setup()
        print("LLM finished setting up.")

    # comparisonsNoThreading()
    # comparisonsThreading()
    vLLMsimultaneousRequests()

def loadModel(args):
    print(f"Total GPU memory: {get_total_gpu_memory()}")

    print("Setup LLM...")

    if (args.inference_provider == "vllm"):
        global vLLM_configurable, llm, samplingparams
        import vLLM_configurable
        if __name__ == "__main__":
            llm = vLLM_configurable.load(model_name=args.model ,dtype=args.dtype, quantization=args.quantization, model_length=args.model_length, gpu_memory_utilization=args.gpu_usage)
            samplingparams = vLLM_configurable.setup()
    elif (args.model == "normistral11b_thinking" and args.inference_provider == "transformers"):
        if (args.inference_provider == "transformers"):
            global normistral11b_configurable
            import normistral11b_configurable
            normistral11b_configurable.setupLLM(quantization=args.quantization, model_length=args.model_length, dtype=args.dtype)
    elif ((args.model == "gpt_oss_20b" or args.model == "gpt_oss_120b") and args.inference_provider == "transformers"):
        global gpt_oss_configurable, tokenizer, model
        import gpt_oss_configurable
        tokenizer, model = gpt_oss_configurable.setupLLM(model=args.model)
    print("LLM finished setting up.")


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Big Comparison script.')
    
    parser.add_argument("--model", type=str, required=True, default="normistral11b_thinking",
                        choices=["normistral11b_thinking", "gpt_oss_20b", "gpt_oss_120b"],
                        help="Set desired model to use for comparisons (e.g., 'normistral11b_thinking', 'gpt_oss_20b', 'gpt_oss_120b').")
    parser.add_argument("--quantization", type=str, required=True, default="full",
                        choices=["4bit", "8bit", "full"],
                        help="Type of quantization (e.g., '4bit', '8bit', 'full')")
    parser.add_argument("--model_length", type=int, default=None,
                        help="Desired model context length (e.g., 4096, 8192, 16384). If not specified, use the default for the model.")
    parser.add_argument("--gpu_usage", type=float, default=0.8,
                        help="Maximum GPU memory usage as a fraction (0-1) to trigger optimizations.")
    parser.add_argument("--inference_provider", type=str, default="transformers", required=True,
                        choices=["transformers", "vllm"], help="Desired inference provider to use for LLM calls.")
    parser.add_argument("--dtype", type=str, required=True, 
                        default="bfloat16", choices=["float16", "bfloat16", "int8", "int4", "half", "auto"],
                        help="Data type for model weights (e.g., 'float16', 'bfloat16', 'int8', 'int4', 'half', 'auto).")
    parser.add_argument("--order", type=str, required=True,
                        default="serial", choices=["serial", "parallel", "xbrl"],
                        help="Order of prompts (e.g., 'serial', 'parallel', 'xbrl').")
    parser.add_argument("--gpu", type=str, required=True,
                        default="h100nv_94GB", choices=["h100nv_94GB", "a100_80GB"],
                        help="Which GPU to run on (e.g., 'h100nv_94GB', 'a100_80GB').")
    
    return parser.parse_args()

def main():
    print("HGello.")

    args = parse_args()
    
    print(f"Model: {args.model}\nQuantization: {args.quantization}\nModel Length: {args.model_length}\nGPU Usage Threshold: {args.gpu_usage}\nInference Provider: {args.inference_provider}\nData Type: {args.dtype}\nOrder: {args.order}\nGPU: {args.gpu}")


    # Configure paths:
    base_path = "/fp/projects01/ec12/mornil/comparisons/comparisonsV2/compResults/"
    special_path = base_path + args.model + "/" + args.inference_provider + "/" + args.order + "/" + str(args.quantization) + "_" + args.model_length.__str__() + "_" + args.gpu_usage.__str__() + "_" + args.dtype + "_" + args.gpu + "/" 
    print(special_path)
    os.makedirs(os.path.dirname(special_path), exist_ok=True)


    # Load model:
    loadModel(args)


    # Run comparisons:
    if (args.order == "serial"):
        comparisonsNoThreading(args, special_path)
    elif (args.order == "parallel"):
        if (args.inference_provider == "vllm"):
            vLLMsimultaneousRequests(args, special_path)
        else:
            comparisonsThreading(args, special_path)
    elif (args.order == "xbrl"):
        xbrlComparisons(args, special_path)

if __name__ == "__main__":
    main()

