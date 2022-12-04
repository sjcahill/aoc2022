# %%
print(ord("a"), ord("A"))
# %%
print(ord("b"), ord("B"))

# %%
print(ord("c") % 32, ord("C") % 32)

# %%
print(ord("d") % 64, ord("D") % 64)
# %%
from string import ascii_letters

charmap = {k: v for k, v in zip(ascii_letters, range(1, 53))}
