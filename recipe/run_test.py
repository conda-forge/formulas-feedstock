import sys

from pathlib import Path
import subprocess

COV_FAIL_UNDER = 71

SKIPS = [
    # https://github.com/conda-forge/formulas-feedstock/pull/17
    # maybe character encoding?
    "test_excel_model",
    "test_ods_model",
    "test_output_025",
    # https://github.com/conda-forge/formulas-feedstock/pull/18
    # maybe character encoding?
    "test_output_001",
    "test_output_022",
    "test_output_023",
    "test_output_024",
    "test_output_026",
    "test_output_027",
    "test_output_028",
    "test_output_029",
    "test_output_030",
    "test_output_031",
    "test_output_032",
    "test_output_033",
    "test_output_034",
    "test_output_035",
    "test_output_036",
    "test_output_037",
    "test_output_038",
    "test_output_039",
    "test_output_040",
    "test_output_174",
    "test_result_01",
    "test_result_02",
    "test_result_03",
    "test_result_04",
    "test_result_05",
    "test_result_06",
    "test_result_07",
    "test_result_08",
    "test_result_09",
    "test_result_10",
    "test_result_11",
    "test_result_12",
    "test_result_13",
]
DELETE = [
    "test/test_readme.py",
    "test/test_setup.py",
]

TEST = [
    "coverage",
    "run",
    "--source=formulas",
    "--branch",
    "-m",
    "pytest",
    "-vv",
    "--tb=long",
    "--color=yes",
    *(
        []
        if not SKIPS
        else ["-k", f"""not ({" or ".join(SKIPS)})""" if len(SKIPS) > 1 else SKIPS[0]]
    ),
]

REPORT = [
    "coverage",
    "report",
    "--show-missing",
    "--skip-covered",
    f"--fail-under={COV_FAIL_UNDER}",
]


def do(args: list[str]) -> int:
    print(">>>", *args, flush=True)
    return subprocess.call(args)


if __name__ == "__main__":
    [(Path.cwd() / d).unlink() for d in DELETE]
    sys.exit(do(TEST) or do(REPORT))
