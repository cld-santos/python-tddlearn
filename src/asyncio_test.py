import asyncio
import time


async def _wait_message(message):
    while True:
        print(message + "    ", end="\r")
        for n in range(4):
            print(message + "." * n, end="\r")
            await asyncio.sleep(0.4)


async def _run(aw):
    await aw
    raise asyncio.CancelledError()


async def run(aw, wait_message="wait"):
    task_wait_message = asyncio.create_task(_wait_message(wait_message))
    task_execute = asyncio.create_task(_run(aw))

    try:
        await task_execute
        await task_wait_message
    except asyncio.CancelledError:
        print(" done" + " " * 80)
    except Exception as e:
        raise e


async def run_list(aws, wait_message="wait"):
    id = 1
    list_aws = []

    for aw in aws:
        list_aws.append(asyncio.create_task(run(aw)))
        id += 1

    try:
        await asyncio.gather(*list_aws)
    except asyncio.CancelledError:
        print("done" + " " * 80)
    except Exception as e:
        raise e


async def main():
    print(f"started at {time.strftime('%X')}")
    await run_list([asyncio.sleep(20), asyncio.sleep(13), asyncio.sleep(2), asyncio.sleep(5), asyncio.sleep(2)], "it takes time, please gather patience")
    await run(asyncio.sleep(2), "it takes time, please await")
    print(f"finish at {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main())
