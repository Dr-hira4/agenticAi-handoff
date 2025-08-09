#LOCAL CONTEXT

from agent import Agent, Runner
import asyncio
from connection import config
from dataclasses import dataclass

@dataclass
class UserInfo:
    name: str
    uid: int

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"user {wrapper.context.name} is 25 years old."

async def main():
    user_info = UserInfo(name="Hira", uid=101)

    agent = Agent[Userinfo](
        name="Assistant",
        instructions="Use the 'fetch_user_age' tool and always only say exactly what the tool returns.",
        tools=[fetch_user_age]
    )

    result = await Runner.run(
        starting_agent=agent,
        input="what is tha age of the user?",
        context=user_info
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())