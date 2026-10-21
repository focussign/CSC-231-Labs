# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 2/2/2026
from measure import FootMeasure
def main():
    moose = FootMeasure(0, 0)
    mason = FootMeasure(0, 90)
    man = FootMeasure(6,23)
    giant = FootMeasure(24,8)
    print(moose) # printing measurements
    print(mason)
    print(man)
    mm = mason + man
    mg = moose + giant
    print(mm) # prints addition
    print(mg)
    moose2 = FootMeasure(0,0)
    giant2 = FootMeasure(24,8)
    print(f'eq dunder: {moose == moose2}') # prints relational operators
    print(f'eq dunder: {giant == giant2}')
    print(f'ne dunder: {moose != giant2}')
    print(f'ne dunder: {moose != moose2}')
    print(f'lt dunder: {moose < giant}')
    print(f'lt dunder: {giant < man}')
    print(f'le dunder: {mason <= giant}')
    print(f'le dunder: {giant <= man}')
    print(f'gt dunder: {giant > man}')
    print(f'gt dunder: {man > mason}')
    print(f'ge dunder: {giant >= mason}')
    print(f'ge dunder: {man >= giant}')

if __name__ == "__main__":
    main()

                  
