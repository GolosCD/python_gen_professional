import traceback

try:
    # some code that could possibly raise an exception
    raise Exception('Exception message')
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    f = traceback.FrameSummary.from_exception(exc_tb)

    print(f"Exception type: {exc_type}")
    print(f"Exception message: {e}")

    # Print the traceback
    print("Traceback (most recent call last):")
    for frame in traceback.extract_tb(exc_tb):
        print(f"\tFile: {frame.filename}, Line: {frame.lineno}, Function: {frame.name}")