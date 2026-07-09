from main import BankAccount

# Each test case is a tuple:
# (description, operations, starting_balance, expected_final_balance, expected_results)
# - operations: list of (op_name, amount)
# - expected_results: list of return values for each operation (deposit -> int new balance, withdraw -> bool)

run_cases = [
    (
        "Simple deposits and withdrawals",
        [("deposit", 50), ("withdraw", 20)],
        100,
        130,
        [150, True],
    ),
    (
        "Over-withdraw should fail",
        [("withdraw", 200)],
        100,
        100,
        [False],
    ),
]

submit_cases = run_cases + [
    (
        "Ignore non-positive amounts",
        [("deposit", 0), ("deposit", -10), ("withdraw", 0), ("withdraw", -5)],
        100,
        100,
        [100, 100, False, False],
    ),
    (
        "Multiple valid operations",
        [("deposit", 50), ("deposit", 25), ("withdraw", 30), ("withdraw", 20)],
        50,
        75,
        [100, 125, True, True],
    ),
    (
        "Withdraw exactly all funds",
        [("withdraw", 100)],
        100,
        0,
        [True],
    ),
    (
        "Mix valid and invalid operations",
        [("deposit", 40), ("withdraw", 200), ("deposit", -5), ("withdraw", 50)],
        100,
        90,
        [140, False, 140, True],
    ),
]


def run_test(description, operations, starting_balance, expected_final, expected_results):
    print("---------------------------------")
    print(f"Test: {description}")
    print("Input operations:")
    for op, amount in operations:
        print(f"  - {op}({amount})")
    print(f"Starting balance: {starting_balance}")
    print("")

    account = BankAccount("Tester", starting_balance)
    actual_results = []

    for op, amount in operations:
        if op == "deposit":
            res = account.deposit(amount)
            actual_results.append(res)
        elif op == "withdraw":
            res = account.withdraw(amount)
            actual_results.append(res)
        else:
            actual_results.append(None)

    final_balance = account.get_balance()

    print(f"Expected final balance: {expected_final}")
    print(f"Actual final balance:   {final_balance}")
    print(f"Expected results: {expected_results}")
    print(f"Actual results:   {actual_results}")

    if final_balance != expected_final:
        return False
    if actual_results != expected_results:
        return False
    return True


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for case in test_cases:
        ok = run_test(*case)
        if ok:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
