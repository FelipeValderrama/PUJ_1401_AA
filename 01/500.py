from io import StringIO
import sys

input_ = map(int, StringIO(sys.stdin.read()))
input_.next()
#l = sys.stdin.read().split[1:]
input_.sort(key=int)
print("\n".join(input_))


