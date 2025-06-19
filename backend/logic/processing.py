def smart_infer(query: str) -> str:
    query_lower = query.lower()

    # Vesting Logic
    if "vesting" in query_lower:
        return (
            "Vesting refers to the process by which you earn the right to own your stock options or RSUs over time. "
            "For example, a 4-year vesting schedule with a 1-year cliff means you get 25% after the first year and monthly vesting thereafter."
        )

    # RSU vs ISO/NSO
    elif "rsu" in query_lower and ("iso" in query_lower or "nso" in query_lower):
        return (
            "RSUs (Restricted Stock Units) are company shares given to employees as part of compensation. "
            "ISOs and NSOs are types of stock options, where ISOs may have tax advantages if held long enough, "
            "while NSOs are more flexible but less tax-efficient."
        )

    # Performance-based grants
    elif "performance" in query_lower and "vesting" in query_lower:
        return (
            "Performance-based vesting means your shares vest based on achieving company or personal milestones, "
            "rather than just time. Common examples include revenue targets, IPO, or product launches."
        )

    # Cliff Vesting
    elif "cliff" in query_lower:
        return (
            "A cliff is the minimum period of time an employee must work before any shares vest. "
            "A 1-year cliff means you receive nothing for the first 12 months, then 25% vests all at once."
        )

    # Taxes
    elif "tax" in query_lower:
        return (
            "Taxation of equity grants depends on type: RSUs are taxed as ordinary income at vesting. "
            "ISOs may be subject to AMT, while NSOs are taxed when exercised based on the spread between strike price and FMV."
        )

    # Default fallback
    else:
        return (
            "I'm not sure how to answer that yet, but I'm learning! Please try rephrasing or contact your HR team."
        )