#!/usr/bin/env python
import psutil
print(x)


def checkcpu():
    x = psutil.cpu_percent()
    psutil.virtual_memory()
    if x > 75:
        return 0
    if x < 75:
        return -1


def main():
    checkcpu()


if __name__ == "__main":
    main(0)
