# !pip install jedi
# #!pip install protobuf==5.29.3
# #!pip install vllm==0.7.0
# !pip install transformers==4.57.6
# !pip install vllm==0.11.0
# #!pip install vllm


from vllm import LLM, SamplingParams
import torch
import time
import datetime

def main():
    print("\nLoading model...\n")
    # load the NorMistral model
    llm = LLM(
        model="norallm/normistral-11b-thinking",
        dtype="half", # prev bfloat16.
        tensor_parallel_size=4,
        gpu_memory_utilization=0.8,
        max_model_len=32768
    )
    print("\nmodel loaded...\n")
    # create a conversation
    messages = [
        {"role": "user", "content": "Hva er hovedstaden i Norge?"},
        {"role": "assistant", "content": "Hovedstaden i Norge er Oslo. Denne byen ligger i den sørøstlige delen av landet, ved Oslofjorden. Oslo er en av de raskest voksende byene i Europa, og den er kjent for sin rike historie, kultur og moderne arkitektur. Noen populære turistattraksjoner i Oslo inkluderer Vigelandsparken, som viser mer enn 200 skulpturer laget av den berømte norske skulptøren Gustav Vigeland, og det kongelige slott, som er den offisielle residensen til Norges kongefamilie. Oslo er også hjemsted for mange museer, gallerier og teatre, samt mange restauranter og barer som tilbyr et bredt utvalg av kulinariske og kulturelle opplevelser."},
        {"role": "user", "content": "Gi meg en liste over de beste stedene å besøke i hovedstaden"}
    ]

    # set up sampling parameters (equivalent to the generate() parameters)
    sampling_params = SamplingParams(
        max_tokens=2048,  # limit max number of generated tokens
        top_k=64,  # top-k sampling
        top_p=0.9,  # nucleus sampling
        temperature=0.3,  # a low temperature to make the outputs less chaotic
        repetition_penalty=1.0,  # turn the repetition penalty off
    )

    # run the generation using the chat interface (applies chat template automatically)
    outputs = llm.chat(messages, sampling_params=sampling_params)

    # get the generated text
    output_str = outputs[0].outputs[0].text.strip()

    # separate the reasoning trace that's enclosed in the special <think> ... </think> tokens
    reasoning_trace = output_str.split("</think>")[0].lstrip("<think>").strip()

    # separate the actual response that follows after the </think> token
    response = output_str.split("</think>")[-1].rstrip("</s>").strip()

    print("\nReasoning trace:\n", reasoning_trace)
    print("Generated response:\n", response)

def load():
  # load the NorMistral model
  llm = LLM(
      model="norallm/normistral-11b-thinking",
      dtype=torch.bfloat16,
      trust_remote_code=True,
    #   quantization="bitsandbytes",
      #load_format="bitsandbytes",
      #dtype="half", # prev bfloat16.
      #tensor_parallel_size=1,
      gpu_memory_utilization=0.8,
      max_model_len=32768 # 16384 funka, 32768 er kanskje bedre.
  )

  print("load done")
  return llm

def setup():

  # set up sampling parameters (equivalent to the generate() parameters)
  sampling_params = SamplingParams(
      max_tokens=2048,  # limit max number of generated tokens
      top_k=64,  # top-k sampling
      top_p=0.9,  # nucleus sampling
      temperature=0.3,  # a low temperature to make the outputs less chaotic
      repetition_penalty=1.0,  # turn the repetition penalty off
  )
  print("setup done")
  return sampling_params



def callvLLM(llm, prompt, sampling_params):
  print("Received prompt: ", prompt)
  #prompt = "Which city is the Eiffel Tower located in?"
  messages = [
      {"role": "user", "content": prompt}
  ]
  # run the generation using the chat interface (applies chat template automatically)
  outputs = llm.chat(messages, sampling_params=sampling_params)

  # get the generated text
  output_str = outputs[0].outputs[0].text.strip()

  # separate the reasoning trace that's enclosed in the special <think> ... </think> tokens
  reasoning_trace = output_str.split("</think>")[0].lstrip("<think>").strip()

  # separate the actual response that follows after the </think> token
  response = output_str.split("</think>")[-1].rstrip("</s>").strip()

  #print("\nReasoning trace:\n", reasoning_trace)
  #print("Generated response:\n", response)

  return response

def makeRequest():
    print("Starting request.")

    start = time.perf_counter()
    starttime = str(datetime.datetime.now())
    result = callvLLM(llm, prompt_big, samplingparams)
    endtime = str(datetime.datetime.now())
    end = time.perf_counter()


    print("\n\nTime taken for comparisons: ", str(end - start), " seconds.\nStarttime: ", starttime, " Endtime: ", endtime)
    print("\n\nResponse: ", result, "\n")

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
    

if __name__ == "__main__":
  llm = load()
  samplingparams = setup()
  makeRequest()

