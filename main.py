import os
import time
from datetime import date

from dotenv import load_dotenv

from Context.Ctx import Ctx
from Core.Robot import Robot
from Core.UserInterface import UserInterface
from Dispatcher.Raya.Executor import Executor
from Dispatcher.Raya.Raya import Dispatcher
from IO.AudioInput import AudioInput
from IO.Output import Output
from Logger.CompositeLogger import CompositeLogger
from Logger.FileLogger import FileLogger
from Logger.MemoryLogger import MemoryLogger
from Logger.StdoutLogger import StdoutLogger
from Memory.JsonMemory import JsonMemory

load_dotenv()


def main():
    if not os.path.isdir("./Logger/logs/{date}".format(date=date.today())):
        os.makedirs("./Logger/logs/{date}".format(date=date.today()))

    memory = JsonMemory()

    logger = CompositeLogger([
        StdoutLogger(),
        FileLogger("./Logger/logs/{date}/raya-{runId}.log".format(date=date.today(), runId=int(time.time()))),
        MemoryLogger(memory),
    ])

    ui = UserInterface(AudioInput('ru-RU'), Output(), logger)

    executor = Executor(Ctx(ui, memory))
    dispatcher = Dispatcher(executor, logger)

    robot = Robot(logger, dispatcher)

    while True:
        robot.run(ui)


if __name__ == "__main__":
    main()
