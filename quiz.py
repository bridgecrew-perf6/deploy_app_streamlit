import streamlit as st
import logging
from random import randint

logger = logging.getLogger(__name__)

st.set_page_config(page_title="Financial Literacy",
                   page_icon=":mortar_board:")
st.title('Improve on your financial language \n ')

# color "st.buttons" in main page light blue:
st.markdown("""
 <style>
 div.stButton > button:first-child {
     background-color: rgb(200, 54, 180); # rgb(216, 78, 192);
 }
 </style>""", unsafe_allow_html=True)
# hide menu
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

# site-structure and main-widgets:
first = st.container()
second = st.container()
end = st.sidebar.button("End")
start = st.sidebar.button("Start")
next = second.button("Next question")

# Dictionary of all countries and capitals in Europe
knowledge = {
    'A type of financial portfolio strategy that involves frequent hands-on strategic intervention — buying and selling assets — from a financial adviser.' : 'Active management', 'your gross income minus certain adjustments, such as deducting student-loan interest' : 'Adjusted gross income', 'A tax that applies to high-income individuals to ensure that they are paying a sufficient amount of tax' : 'Alternative minimum tax', 'The process by which the amount due on a loan is reduced over time' : 'Amortization',
    'the total amount it will cost you to borrow money, be it through a loan, credit card, or other instruments, each year' : 'Annual Percentage Rate', 'A financial instrument, typically offered through an insurance company, that guarantees a certain payout, either in a lump sum or in increments' : 'Annuity', 'An increase in the value of a particular asset over time' : 'Appreciation', "A payment method where the payer pays the payee after the work they're being paid for has been completed" : 'Arrears',
    'The lowest dollar amount the seller of a security will accept in exchange for that security' : 'Ask price', 'An item a person or entity owns that has financial value or is expected to have financial value in the future' : 'Asset', "A document that provides prospective investors with a summary of a company's financial standing by detailing its assets, liabilities, and shareholders' equity" :'Balance sheet', 'A legal proceeding that gives a person or business who can no longer pay their debts a chance to be released from the responsibility of paying those debts': 'Bankruptcy',
    'A way of describing the state of the stock market that indicates that stocks are declining in value overall' : 'Bear market', 'The recipient of an item or asset, generally after its original owner has died' : 'Beneficiary', 'The highest amount a prospective buyer of a security will consider paying for that security' : 'Bid price', 'A term used to refer to companies whose stock is considered a solid investment' : 'Blue chip',
    'An investment strategy that focuses on the performance of individual companies and their stock rather than on market trends on the whole' : 'Bottom-up investing', "An individual or organization that facilitates the buying and selling of assets on someone else's behalf" : 'Broker', 'A way of describing the state of the stock market that indicates stocks are increasing in value' : 'Bull market',
    'The profit that results from selling an asset that has grown in value' : 'Capital gain', 'The loss an investor experiences when they sell an asset that has lost value' : 'Capital loss', 'The interest periodically added to the total balance of a loan. For student loans, this often happens at the end of the initial grace period' : 'Capitalised interest', "The movement of a person's, household's, or business's money—coming in as income and going out as expenses" : 'Cash flow',
    "A borrower's item, property, or asset that a lender accepts as a guarantee of a loan" : 'Collateral', 'The fee that a financial-services company pays a financial adviser when the adviser sells a product to a client' : 'Commission', 'An economic unit that can be bought or sold but has the same value regardless of who produced it' : 'Commodity', 'A method of calculating interest where you earn a percentage not just of the principal amount but the principal plus any previously earned interest' : 'Compound interest',
    'The amount an investor paid for a security, including broker commissions and other fees and adjustments' : 'Cost basis', 'The record of your credit usage habits over time that includes a list of all your credit accounts' : 'Credit history', 'The annual reports performed by each of the three credit bureaus that show all your credit accounts in one place' : 'Credit report', 'The three-digit score assigned to your credit profile based on your debt history' : 'Credit score',
    'A form of decentralized digital currency not tied to any nation or standard' : 'Cryptocurrency', 'A financial account that belongs to a minor but is run by a designated adult until the minor reaches an age set by the terms of the account' : 'Custodial account', 'he total amount of your monthly liabilities (mortgage, credit card debt, student loans, and any other money you owe on a monthly basis) divided by the amount that you earn each month before taxes' : 'Debt-to-income ratio', 'The amount you must pay out of pocket before your insurance coverage kicks in and covers the rest' : 'Deductible',
    'A decline in the value of a particular asset over time' : 'Depreciation', 'The earned money left over after taxes, health insurance, rent or a mortgage payment, and all other living expenses have been covered' : 'Discretionary income', 'The payouts companies make on a recurring basis to the investors who own their shares' : 'Dividends', 'The lump sum of money you pay toward buying a home when you take out a mortgage' : 'Down payment',
    'Mortgage is a loan taken to purchase property and guaranteed by the same property' : 'Mortgage', "Your ownership of an asset after you've accounted for the debt you owe on it" : 'Equity', 'The process of preparing your finances for when you die' : 'Estate planning', 'Money that an individual or entity owes someone else' : 'Liability',
    'A term that describes how quickly and easily you can pull cash out of a particular asset' : 'Liquidity', 'The total value of all of your assets wage income, investments, property minus the total amount of your debt' : 'Net worth', 'A deficit that occurs when you withdraw an amount of money from an account that exceeds the account balance' : 'Overdraft'
    }

# initiate necessary session_state-variables #########
if 'countries' not in st.session_state:
    st.session_state['countries'] = list(knowledge.keys())
# number of questions asked:
if 'questions' not in st.session_state:
    st.session_state['questions'] = 0
if 'right' not in st.session_state:
    st.session_state['right'] = 0
if 'wrong' not in st.session_state:
    st.session_state['wrong'] = 0
if 'capital' not in st.session_state:
    st.session_state['capital'] = ""
if 'last' not in st.session_state:
    st.session_state['last'] = "last"
# 'number' stores the number of countries remaining:
if 'number' not in st.session_state:
    st.session_state['number'] = len(st.session_state['countries'])-1
# select a random item out of the coutries list:
x = randint(0, st.session_state['number'])
# 'country' stores the country in the current question:
if 'concept' not in st.session_state:
    st.session_state['concept'] = st.session_state['countries'][x]

def new():
    try:
        x = randint(0, st.session_state['number'])
    except:
        quit()
    st.session_state['concept'] = st.session_state['countries'][x]

def grade(perc):
    if perc == 100:
        grade = "fantastic! (⊃｡•́‿•̀｡)⊃"
    elif perc > 80:
        grade = "very good! (ɔ ᵔᴗᵔ)ɔ"
    elif perc > 70:
        grade = "good! ( ͡° ͜ ͡°)"
    elif perc >= 50:
        grade = "ok! (~ • ᴥ •)~"
    elif perc > 30:
        grade = "not so good! (｡ŏ﹏ŏ)"
    elif perc > 20:
        grade = "bad! (ɔ ᴗ_ᴗ)ɔ"
    else:
        grade = "poor! (ɔ •︵•)ɔ"
    return grade

def reset():
    # reset values:
    st.session_state['concept'] = list(knowledge.keys())
    st.session_state['number'] = len(st.session_state['countries'])-1
    st.session_state['questions'] = 0
    st.session_state['right'] = 0
    st.session_state['wrong'] = 0
    st.session_state['capital'] = ""

def main():
    concept = st.session_state['concept']
    first.markdown(f"{concept}?")
    capital = first.text_input("", "", key=st.session_state['questions'])
    if capital != st.session_state['last'] and capital != "":
        st.session_state['last'] = capital
        st.session_state['questions'] += 1
        st.session_state['capital'] = capital
        if st.session_state['capital'] == knowledge[concept]:
            st.session_state['countries'].remove(concept)
            st.session_state['right'] += 1
            st.session_state['number'] -= 1
            if st.session_state['number'] == -1:
                perc = st.session_state['right'] * 100 / st.session_state['questions']
                second.write(f"You know all the capitals in Europe (ɔ °0°)ɔ\nand have {st.session_state['right']} from {st.session_state['questions']} questions answered correctly ({int(round(perc,0))} percent).")
                second.write(f"That is {grade(perc)}")
                reset()
            else:
                second.write("That's right. (✿^‿^)")
                second.write(f"{st.session_state['right']} from {st.session_state['questions']} (still {str(st.session_state['number']+1)} questions)")

        else:
            st.session_state['wrong'] += 1
            second.write(f"'{capital}' is false. (ɔ •︵•)ɔ \n {concept} is: {knowledge[st.session_state['concept']]}")
            second.write(f"{st.session_state['right']} from {st.session_state['questions']} (still {str(st.session_state['number']+1)} questions)")

def quit():
    try:
        perc = st.session_state['right'] * 100 / st.session_state['questions']
    except:
        perc = 0
    second.write(f"You have {st.session_state['right']} from {st.session_state['questions']} questions answered correctly ({int(round(perc,0))} Percent).")
    second.write(f"That is {grade(perc)}")
    reset()

if end:
    quit()

if start:
    new()

if next:
    new()

#########################################################################
if __name__ == '__main__':
    main()