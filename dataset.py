# Menu with IDs
menu = [
    {"id": 1, "question": "Mutual Funds Overview"},
    {"id": 2, "question": "SIP, NAV, Lumpsum"},
    {"id": 3, "question": "Mutual Fund Returns"},
    {"id": 4, "question": "Taxation on Mutual Funds"},
    {"id": 5, "question": "Mutual Fund Investment Methods"},
    {"id": 6, "question": "Mutual Fund Liquidity"},
    {"id": 7, "question": "Other Banks Mutual Funds"}
]

# Questions Data
questions_data = {
    1: [{"id": 101, "question": "What is a mutual fund?"},
        {"id": 102, "question": "What are the types of mutual funds?"},
        {"id": 103, "question": "How do mutual funds work?"}],
    2: [{"id": 104, "question": "What is an SIP?"}, {"id": 105, "question": "What is NAV?"},
        {"id": 106, "question": "What is Lumpsum?"}],
    3: [{"id": 107, "question": "How are mutual fund returns calculated?"},
        {"id": 108, "question": "What is the expense ratio in a mutual fund?"}],
    4: [{"id": 109, "question": "How are mutual funds taxed?"},
        {"id": 110, "question": "Does the Fund Offer Tax Advantages?"},
        {"id": 111, "question": "How are mutual fund dividends taxed?"}],
    5: [{"id": 112, "question": "How can I invest in mutual funds?"},
        {"id": 113, "question": "What is the difference between actively managed and passively managed mutual funds?"},
        {"id": 114, "question": "What are capital gains in mutual funds?"}],
    6: [{"id": 115, "question": "Can I withdraw my mutual fund investment anytime?"},
        {"id": 116, "question": "Can I withdraw my mutual fund investment anytime?"},
        {"id": 117, "question": "What is a liquid fund?"}]
}

# Answers Data
answers_data = {
    101: "A mutual fund is an investment vehicle that pools money from various investors to invest in a diversified "
         "portfolio of assets such as stocks, bonds, and other securities. The fund is managed by a professional fund "
         "manager. Each investor owns units of the mutual fund in proportion to their investment, and they earn "
         "returns based on the performance of the assets held within the fund.",
    102: "Types of mutual funds include equity funds which are Primarily invest in stocks for capital appreciation , "
         "Debt funds which are Invest in bonds and other debt instruments, offering lower risk and steady returns and "
         "Hybrid funds in which it Invest in a mix of equity and debt to balance risk and returns.",
    103: "When you invest in a mutual fund, your money is combined with that of other investors. The fund manager "
         "uses this pooled money to buy a variety of securities (like stocks and bonds). As these investments grow or "
         "lose value, so does the value of your shares in the mutual fund.",
    104: "A Systematic Investment Plan (SIP) is a way of investing in mutual funds regularly. You invest a fixed "
         "amount of money at regular intervals (e.g., monthly), which helps build wealth over time with the benefit "
         "of compounding.",
    105: "Net Asset Value (NAV) is the per-unit value of a mutual fund. It is calculated by dividing the total value "
         "of the fund's assets minus its liabilities by the total number of units or shares outstanding.",
    106: "A lump sum is a single payment of money made at one time, rather than in installments. It can be used for "
         "investments, loans, insurance, retirement, and more. ",
    107: '''Mutual fund returns are generally calculated based on the change in the fund's Net Asset Value (NAV) over a certain period. The formula to calculate the return is:
Return=(Ending NAV - Beginning NAV) + DividendsBeginning NAV×100
Return= Beginning NAV(Ending NAV - Beginning NAV) + Dividends×100
Dividends and capital gains are typically distributed to investors, and they also contribute to the total return.''',
    108: "The expense ratio is the annual fee charged by a mutual fund to manage the fund's assets. It is expressed "
         "as a percentage of the fund's average assets under management (AUM) and covers management fees, "
         "administrative costs, and other expenses. A lower expense ratio generally means more of your investment "
         "goes toward actual returns.",
    109: "Mutual funds are taxed based on the type of fund and holding period.",
    110: "ELSS mutual funds under Section 80C offer tax benefits. Tax efficiency depends on strategy, turnover ratio, "
         "and distribution type, with index funds being more tax-efficient than actively managed ones. Choosing a "
         "low-turnover, tax-efficient fund helps maximize returns.ELSS mutual funds under Section 80C offer tax "
         "benefits."
         "Tax efficiency depends on strategy, turnover ratio, and distribution type, with index funds being more "
         "tax-efficient than actively managed ones. Choosing a low-turnover, tax-efficient fund helps maximize returns.",
    111: "Mutual fund dividends are taxed as regular income, while profits from redeemed units are subject to capital "
         "gains tax, varying by holding period.",
    112: "You can invest through online platforms, banks, AMCs, or brokers.",
    113: '''Actively Managed Funds: A fund manager actively buys and sells securities to try to outperform the market. These funds typically have higher management fees due to the active decision-making process.
Passively Managed Funds: These funds aim to replicate the performance of a market index (e.g., the S&P 500) rather than trying to outperform it. They usually have lower fees because there's less active management involved.
''',
    114: "Capital gains are the profits made from the sale of securities within a mutual fund when their selling "
         "price exceeds the purchase price. Mutual funds typically distribute capital gains to investors at the end "
         "of the year. These gains are either long-term (if the securities are held for more than a year) or "
         "short-term (if held for less than a year), and they may be subject to different tax rates.",
    115: "Most open-ended mutual funds allow withdrawal anytime, but exit loads may apply.",
    116: "Yes, many retirement accounts like IRAs or 401(k)s allow you to invest in mutual funds. In fact, "
         "mutual funds are often one of the most common investment options in retirement plans because they offer "
         "diversification and professional management. Be sure to check your plan’s available mutual fund options and "
         "contribution limits.",
    117: "A liquid fund is a type of mutual fund that invests in short-term debt instruments, such as Treasury bills, "
         "certificates of deposit, and commercial paper. These funds offer high liquidity (easy to convert into cash) "
         "and low risk, making them ideal for parking short-term funds or for investors looking for a safe, low-return "
         "option."
}

# Exit message
exit_message = "Thank you for using Fino! Have a great day!"

Other_mutualFunds = "Other Banks Mutual Funds Websites were includes •\tICICI Bank  " \
                    "->https://www.icicipruamc.com/\n•\tSBI (State Bank of India) ->https://www.sbimf.com/\n•\tAxis " \
                    "Bank  ->https://www.axismf.com/\n•\tKotak Mahindra Bank  ->https://www.kotakmf.com/\n•\tBank of " \
                    "Baroda-> https://www.bankofbaroda.in/personal-banking/investments/investment-products/mutual" \
                    "-fund-investment\n•\tPunjab National Bank (PNB)  ->https://www.pnbindia.in/mutual-fund.html"
