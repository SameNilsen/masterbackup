#!pip install transformers==4.57.6
#!pip install -U bitsandbytes
#!pip install accelerate
#!pip install langchain-huggingface

import torch
import transformers
from transformers import (
  AutoTokenizer,
  AutoModelForCausalLM,
  BitsAndBytesConfig,
  pipeline
)

from transformers import BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline

#from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate

import nest_asyncio

def setupLLM():
    #################################################################
    # Tokenizer
    #################################################################

    ## I denne variabelen setter man LLM modellen.
    ## Om man skal bruke nb-gpt: model_name='NbAiLab/nb-gpt-j-6B'
    global model_name
    #model_name='norallm/normistral-7b-warm-instruct'
    model_name='Qwen/Qwen3-8B'

    model_config = transformers.AutoConfig.from_pretrained(
        model_name,
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"




    #################################################################
    # bitsandbytes parameters
    #################################################################

    # Activate 4-bit precision base model loading
    use_4bit = True

    # Compute dtype for 4-bit base models
    bnb_4bit_compute_dtype = "float16"

    # Quantization type (fp4 or nf4)
    bnb_4bit_quant_type = "nf4"

    # Activate nested quantization for 4-bit base models (double quantization)
    use_nested_quant = False

    #################################################################
    # Set up quantization config
    #################################################################
    compute_dtype = getattr(torch, bnb_4bit_compute_dtype)

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=use_4bit,
        bnb_4bit_quant_type=bnb_4bit_quant_type,
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_use_double_quant=use_nested_quant,
    )

    # Check GPU compatibility with bfloat16
    if compute_dtype == torch.float16 and use_4bit:
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            print("=" * 80)
            print("Your GPU supports bfloat16: accelerate training with bf16=True")
            print("=" * 80)

    #################################################################
    # Load pre-trained config
    #################################################################
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map='auto',
        torch_dtype=torch.bfloat16
    )

    ## Setter chat template for norallm/normistral-7b-warm-instruct, med en annen modell er det mulig denne må endres.
    messages = [
        {"role": "user", "content": "Hva er hovedstaden i Norge?"},
        {"role": "assistant", "content": "Hovedstaden i Norge er Oslo. Denne byen ligger i den sørøstlige delen av landet, ved Oslofjorden. Oslo er en av de raskest voksende byene i Europa, og den er kjent for sin rike historie, kultur og moderne arkitektur. Noen populære turistattraksjoner i Oslo inkluderer Vigelandsparken, som viser mer enn 200 skulpturer laget av den berømte norske skulptøren Gustav Vigeland, og det kongelige slott, som er den offisielle residensen til Norges kongefamilie. Oslo er også hjemsted for mange museer, gallerier og teatre, samt mange restauranter og barer som tilbyr et bredt utvalg av kulinariske og kulturelle opplevelser."},
        {"role": "user", "content": "Gi meg en liste over de beste stedene å besøke i hovedstaden"}
    ]
    #gen_input = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
    #print("-----------GENINPUT", gen_input)


    print(print_number_of_trainable_model_parameters(model))


    ## Om man skal bytte LLM må man påse at disse parameterene er satt riktig.
    ## De som er satt her er det som ble anbefalt for normistral instruct: https://huggingface.co/norallm/normistral-7b-warm-instruct
    #text_generation_pipeline = pipeline(
    #    model=model,
    #    task="text-generation",
    #    tokenizer=tokenizer,
    #    max_new_tokens=2048,
    #    top_k=20,  # top-k sampling
    #    top_p=0.95,  # nucleus sampling
    #    temperature=0.6,  # a low temparature to make the outputs less chaotic
    #    repetition_penalty=1.0,  # turn the repetition penalty off, having it on can lead to very bad outputs
    #    do_sample=True,  # randomly sample the outputs
    #    use_cache=True,  # speed-up generation
    #)

    #mistral_llm = HuggingFacePipeline(pipeline=text_generation_pipeline)

    ## Jeg aner ikke hva dette brukes til...
    import nest_asyncio
    nest_asyncio.apply()

    # Legg til model, tokenizer for contextcite.
    return model, tokenizer


def print_number_of_trainable_model_parameters(model):
    trainable_model_params = 0
    all_model_params = 0
    for _, param in model.named_parameters():
        all_model_params += param.numel()
        if param.requires_grad:
            trainable_model_params += param.numel()
    return f"trainable model parameters: {trainable_model_params}\nall model parameters: {all_model_params}\npercentage of trainable model parameters: {100 * trainable_model_params / all_model_params:.2f}%"


def askLLM(model, tokenizer):
  while True:
        question = input(f"\n -> Spør {model_name} LLM et spørsmål: ")
        if question.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        # prepare the model input
        prompt = "Give me a short introduction to large language model."
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
        messages = [
            {"role": "user", "content": prompt_big}
        ]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

        # conduct text completion
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=32768
        )
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

        # parsing thinking content
        try:
            # rindex finding 151668 (</think>)
            index = len(output_ids) - output_ids[::-1].index(151668)
        except ValueError:
            index = 0

        thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
        content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

        print("thinking content:", thinking_content)
        print("content:", content)

print("Setting up LLM")
model, tokenizer = setupLLM()

askLLM(model, tokenizer)
