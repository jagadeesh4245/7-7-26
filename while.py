# =========================================================
# 35 Pattern Programs - ONLY while loops, NO function defs
# =========================================================

# 1. Solid Square Pattern
n = 4
print("1. Solid Square")
i = 1
while i <= n:
    j = 1
    while j <= n:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# 2. Solid Rectangle Pattern
m = 3
n = 5
print("\n2. Solid Rectangle")
i = 1
while i <= m:
    j = 1
    while j <= n:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# 3. Right-Angled Triangle (Left-Aligned)
n = 5
print("\n3. Triangle Left")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# 4. Right-Angled Triangle (Right-Aligned)
n = 5
print("\n4. Triangle Right")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# 5. Inverted Triangle (Left-Aligned)
n = 5
print("\n5. Inverted Triangle Left")
i = n
while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

# 6. Inverted Triangle (Right-Aligned)
n = 5
print("\n6. Inverted Triangle Right")
i = n
while i >= 1:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

# 7. Centered Pyramid Pattern
n = 4
print("\n7. Pyramid")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k += 1
    print()
    i += 1

# 8. Diamond Pattern
n = 3
print("\n8. Diamond")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k += 1
    print()
    i += 1
i = n - 1
while i >= 1:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k += 1
    print()
    i -= 1

# 9. Butterfly Pattern
n = 4
print("\n9. Butterfly")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    j = 1
    while j <= 2 * (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
i = n
while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    j = 1
    while j <= 2 * (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

# 10. Left-Aligned Half Diamond
n = 4
print("\n10. Half Diamond Left")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
i = n - 1
while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

# 11. Right-Aligned Half Diamond
n = 4
print("\n11. Half Diamond Right")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
i = n - 1
while i >= 1:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

# 12. Sandglass Pattern
n = 4
print("\n12. Sandglass")
i = n
while i >= 1:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1
i = 2
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# 13. Increasing Width Triangle
n = 5
print("\n13. Increasing Width Triangle")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# 14. Decreasing Width Triangle
n = 5
print("\n14. Decreasing Width Triangle")
i = n
while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

# 15. Right-Aligned Hill Pattern
n = 4
print("\n15. Hill Right")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# 16. Hollow Square Pattern
n = 4
print("\n16. Hollow Square")
i = 1
while i <= n:
    j = 1
    while j <= n:
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1

# 17. Hollow Rectangle Pattern
m = 4
n = 5
print("\n17. Hollow Rectangle")
i = 1
while i <= m:
    j = 1
    while j <= n:
        if i == 1 or i == m or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1

# 18. Hollow Right-Angled Triangle (Left-Aligned)
n = 5
print("\n18. Hollow Triangle Left")
i = 1
while i <= n:
    j = 1
    while j <= i:
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1

# 19. Hollow Right-Angled Triangle (Right-Aligned)
n = 5
print("\n19. Hollow Triangle Right")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= i:
        if k == 1 or k == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k += 1
    print()
    i += 1

# 20. Hollow Inverted Triangle (Left-Aligned)
n = 5
print("\n20. Hollow Inverted Triangle Left")
i = n
while i >= 1:
    j = 1
    while j <= i:
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i -= 1

# 21. Hollow Inverted Triangle (Right-Aligned)
n = 5
print("\n21. Hollow Inverted Triangle Right")
i = n
while i >= 1:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= i:
        if k == 1 or k == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k += 1
    print()
    i -= 1

# 22. Hollow Pyramid Pattern
n = 4
print("\n22. Hollow Pyramid")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        if k == 1 or k == (2 * i - 1) or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k += 1
    print()
    i += 1

# 23. Hollow Diamond Pattern
n = 3
print("\n23. Hollow Diamond")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        if k == 1 or k == (2 * i - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k += 1
    print()
    i += 1
i = n - 1
while i >= 1:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        if k == 1 or k == (2 * i - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k += 1
    print()
    i -= 1

# 24. Hollow Butterfly Pattern
n = 4
print("\n24. Hollow Butterfly")
i = 1
while i <= n:
    j = 1
    while j <= i:
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    j = 1
    while j <= 2 * (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1
i = n
while i >= 1:
    j = 1
    while j <= i:
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    j = 1
    while j <= 2 * (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i -= 1

# 25. Hollow Hourglass Pattern
n = 5
print("\n25. Hollow Hourglass")
i = 1
while i <= n:
    if i == 1:
        j = 1
        while j <= n:
            print("*", end=" ")
            j += 1
    else:
        j = 1
        while j <= (i - 2):
            print(" ", end=" ")
            j += 1
        if i == n:
            j = 1
            while j <= (n - 2 * (i - 1)):
                print(" ", end=" ")
                j += 1
            print("*", end=" ")
        else:
            print("*", end=" ")
            j = 1
            while j <= (n - 2 * i):
                print(" ", end=" ")
                j += 1
            print("*", end=" ")
    print()
    i += 1
i = n - 1
while i >= 1:
    if i == 1:
        j = 1
        while j <= n:
            print("*", end=" ")
            j += 1
    else:
        j = 1
        while j <= (i - 2):
            print(" ", end=" ")
            j += 1
        print("*", end=" ")
        j = 1
        while j <= (n - 2 * i):
            print(" ", end=" ")
            j += 1
        print("*", end=" ")
    print()
    i -= 1

# 26. Increasing Number Triangle
n = 5
print("\n26. Num Triangle Increasing")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

# 27. Repeating Row Number Triangle
n = 5
print("\n27. Num Triangle Repeat Row")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1

# 28. Continuous Number Triangle
n = 4
print("\n28. Num Triangle Continuous")
num = 1
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1

# 29. Reverse Row Number Triangle
n = 5
print("\n29. Num Triangle Reverse Row")
i = 1
while i <= n:
    j = i
    while j >= 1:
        print(j, end=" ")
        j -= 1
    print()
    i += 1

# 30. Inverted Number Triangle
n = 5
print("\n30. Num Triangle Inverted")
i = n
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1

# 31. Right-Aligned Number Triangle
n = 5
print("\n31. Num Triangle Right Aligned")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

# 32. Pyramid Number Pattern
n = 4
print("\n32. Num Pyramid")
i = 1
while i <= n:
    j = 1
    while j <= (n - i):
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= i:
        print(k, end=" ")
        k += 1
    k = i - 1
    while k >= 1:
        print(k, end=" ")
        k -= 1
    print()
    i += 1

# 33. Even Number Triangle
n = 5
print("\n33. Even Num Triangle")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(2 * j, end=" ")
        j += 1
    print()
    i += 1

# 34. Odd Number Triangle
n = 5
print("\n34. Odd Num Triangle")
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(2 * j - 1, end=" ")
        j += 1
    print()
    i += 1

# 35. Pascal's Triangle
n = 5
print("\n35. Pascal's Triangle")
i = 0
while i < n:
    val = 1
    j = 0
    while j <= i:
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
        j += 1
    print()
    i += 1


