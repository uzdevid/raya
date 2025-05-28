import os
import time
from datetime import date

from dotenv import load_dotenv

from Context.Ctx import Ctx
from Core.Robot import Robot
from Core.UserInterface import UserInterface
from Dispatcher.Raya.Executor import Executor
from Dispatcher.Raya.Raya import Dispatcher
from IO.Input import Input
from IO.Output import Output
from Logger.CompositeLogger import CompositeLogger
from Logger.FileLogger import FileLogger
from Logger.MemoryLogger import MemoryLogger
from Memory.JsonMemory import JsonMemory


load_dotenv()

def main():
    memory = JsonMemory()

    if not os.path.isdir("./Logger/logs/{date}".format(date=date.today())):
        os.makedirs("./Logger/logs/{date}".format(date=date.today()))

    logger = CompositeLogger(
        fileLogger=FileLogger("./Logger/logs/{date}/raya-{runId}.log".format(date=date.today(), runId=int(time.time()))),
        memoryLogger=MemoryLogger(memory)
    )

    ui = UserInterface(Input('ru-RU'), Output(), logger)

    executor = Executor(Ctx(ui, memory))
    dispatcher = Dispatcher(executor, logger)

    robot = Robot(logger, dispatcher)

    while True:
        robot.run(ui)


if __name__ == "__main__":
    main()
