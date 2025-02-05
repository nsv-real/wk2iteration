from logger import logger
def skip_intergers(*args):
    """
    """
    if not args:
        logger.info(f"Returning early. Empty list argument provided in `skip_integers`")

    logger.info("Starting iteration")
    logger.info(f"List of args is {len(args)} element(s) long.")

    for i in args:
        if isinstance(i, int):
            continue
        else:
            logger.info(f"{i}")
    
    logger.info("Iteration finished")

def main():
    l1 = [1, 5.0, "a", 4, 8, 10, 11.0, 22.0, 23.0]
    skip_intergers(*l1, 5.0, 20.0)

if __name__ == "__main__":
    main()



