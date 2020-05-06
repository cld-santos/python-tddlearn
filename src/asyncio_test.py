import asyncio


async def _wait_message(message):
    try:
        while True:
            print(message + "    ", end="\r")
            for n in range(4):
                print(message + "." * n, end="\r")
                await asyncio.sleep(0.4)
    except:
        pass

async def _run(aw, task):
    await aw
    task.cancel()

async def run(aw, wait_message="wait"):
    task_wait_message = asyncio.create_task(_wait_message(wait_message))
    task_execute = asyncio.create_task(_run(aw, task_wait_message))

    await task_wait_message
    await task_execute

    print("done" + " " * 80)


async def main():
    await run(asyncio.sleep(10), "it takes time, please wait")


if __name__ == "__main__":
    asyncio.run(main())
