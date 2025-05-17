import argparse, string, random, pyperclip, logging
from datetime import datetime

class NoOpLogger:
    def debug(self, *args, **kwargs): pass
    def info(self, *args, **kwargs): pass
    def warning(self, *args, **kwargs): pass
    def error(self, *args, **kwargs): pass
    def critical(self, *args, **kwargs): pass

def setup_logging(logfile=None, debug=False):
    if not logfile:
        timestamp = datetime.now().strftime("lockr_%Y-%m-%d_%H-%M-%S.log")
        logfile = timestamp

    log_level = logging.DEBUG if debug else logging.INFO

    formatter = logging.Formatter("[%(asctime)s] - [%(levelname)s] - %(message)s", "%H:%M:%S")

    # File handler
    file_handler = logging.FileHandler(logfile, mode="w")
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger("lockr")
    logger.setLevel(log_level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.propagate = False  # Prevent duplicate logs

    logger.debug(f"Logging initialized. Output to '{logfile}'")
    return logger

def main():
    parser = argparse.ArgumentParser(description="LOCKR - Rapid password generator")

    parser.add_argument("length", type=int, help="Password length (12–20)")
    parser.add_argument("--remove-special", action="store_true", help="Remove special characters")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--logfile", type=str, help="Custom log file path")

    args = parser.parse_args()

    logger = setup_logging(logfile=args.logfile, debug=args.debug) if args.debug or args.logfile else NoOpLogger()
    logger.info(f"Arguments: {args}")

    characters = list(string.ascii_letters + string.digits + string.punctuation)

    if args.length < 12 or args.length > 20:
        print("Invalid input: Password length must be between 12 and 20")
        logger.error("Invalid password length")
        logger.info("Exiting...")
        exit()

    if args.remove_special:
        characters = [c for c in characters if c not in string.punctuation]
        logger.info("Special characters removed")

    password = "".join(random.choice(characters) for _ in range(args.length))
    logger.info("Password generated")

    pyperclip.copy(password)
    logger.info("Password copied to clipboard")

    print("\nYour password has already been copied to your clipboard ;)")

if __name__ == "__main__":
    main()