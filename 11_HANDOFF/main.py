from agent import Agent, Runner
from connection import config
import asyncio

#srf LLM context:instructions de rahe haoin agents ko

billing_agent = Agent(
    name="Billing Agent",
    instructions="Ap srf billing se related sawalon ka jawab denge."
)

refund_agent = Agent(
    name="Refund Agent",
    instructions="Ap srf refund process karne me madad karenge."
)

triage_agent = Agent(
    name="Triage Agent",
    instruction="Ap user ki request parhen or decide karen k kis agent ko ye kam dena hai.",
    handoffs=[billing_agent, refund_agent]
)


async def main():
    reault = await Runner.run(triage_agent,
                              "why is my bill so high?",
                               run_config=config)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())