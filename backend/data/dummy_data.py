defined_queries = [
    {
        "user_id": "user1",
        "query": "How many grants do I have?",
        "expected_response": "You currently have 3 active equity grants."
    },
    {
        "user_id": "user2",
        "query": "What is the difference between ISO and NSO?",
        "expected_response": "ISOs (Incentive Stock Options) are eligible for special tax treatment, while NSOs (Non-qualified Stock Options) are not."
    },
    {
        "user_id": "user3",
        "query": "What is my vesting schedule?",
        "expected_response": "Your vesting schedule follows a 4-year schedule with a 1-year cliff."
    },
    {
        "user_id": "user4",
        "query": "When can I exercise my options?",
        "expected_response": "You can exercise your options after they have vested, typically after your 1-year cliff."
    },
]

undefined_queries = [
    {
        "user_id": "user1",
        "query": "Can you compare my grant with someone else in my team?",
        "expected_response": "This requires deeper context. Let's analyze historical grant data to make a comparison."
    },
    {
        "user_id": "user2",
        "query": "What’s the optimal strategy for early exercising?",
        "expected_response": "That depends on your tax bracket, current valuation, and expected company growth. Here's a simulation..."
    },
    {
        "user_id": "user3",
        "query": "What are the tax implications if I move to another country?",
        "expected_response": "Tax implications vary by jurisdiction. Let's break this down by your grant type and target country."
    },
    {
        "user_id": "user4",
        "query": "Should I accept the new grant offer or negotiate?",
        "expected_response": "Let’s evaluate your current offer, market benchmarks, and negotiation options."
    }
]

def get_sample_queries():
    return defined_queries + undefined_queries
