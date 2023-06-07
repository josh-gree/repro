from prefect import flow, task, get_run_logger


@task
def say_hello():
    logger = get_run_logger()

    logger.info("From FREYA")


@flow
def repro():
    say_hello()


if __name__ == "__main__":
    repro()
