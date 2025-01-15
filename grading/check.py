import utils
import resource
import subprocess
import argparse

# 195 MiB of memory
BYTES = 195 * 1024 * 1024

def check_exercise(ch, ex):
    try:
        # compile
        task = utils.compile(target=utils.get_ex(ch, ex))
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        
        # run test
        task = utils.run_program(command='cat ' + utils.get_in(ch, ex) + ' | ./a.out')
        if task.returncode != 0:
            print( task.stderr.decode().strip() )
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        
        # output
        output = task.stdout.decode().strip()
        f = open(utils.get_out(ch, ex), 'r')
        expected = f.read().strip()
        f.close()

        points = 0
        if (ch == 1):
            points = 10
        elif (ch == 2) or (ch == 3) or (ch == 4):
            points = 33.34
        else:
            points = -1

        #print("INICIO", output, "FIN", len(output), sep="")
        #print("INICIO", expected, "FIN", len(expected), sep="")

        if output == expected:
            return (points, utils.passed(), '')
        else:
            return (0, utils.failed(f"Error in chapter {ch} exercise {ex}"), '')
    except subprocess.TimeoutExpired:
        return(0, utils.failed('timeout'), '')
    except Exception as e:
        print(e)
        return(0, utils.failed('some other error ocurred'), '')



def ch1(all=False):
    exercises = [8, 9, 10, 12, 13, 14, 15, 17, 19, 20]
    not_found = utils.expected_files(['./ch1/ex-1.8.c', './ch1/ex-1.9.c', './ch1/ex-1.10.c', './ch1/ex-1.12.c', './ch1/ex-1.13.c', './ch1/ex-1.14.c', './ch1/ex-1.15.c', './ch1/ex-1.17.c', './ch1/ex-1.19.c', './ch1/ex-1.20.c'])

    if len(not_found) == 0:
        table = []

        grade = 0
        errors = ''

        for ex in exercises:
            res = check_exercise(1, ex)
            table.append([f"ex 1.{ex}", res[0], res[1]])
            grade += res[0]
            errors += '\n' + utils.create_error(f"ex 1.{ex}", res[2])

        errors = errors.strip()
        grade = min(grade, 100)
        report = utils.report(table)
        print(report)
        
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        
        if all:
            return grade
        else:
            utils.write_result(grade, report, 'chapter1.json')
            return grade

    else:
        utils.write_result(0, 'missing files in chapter 1: %s' % (','.join(not_found)), 'chapter1.json')



def ch2(all=False):
    exercises = ['atoi', 'squeeze', 'concat']
    not_found = utils.expected_files([])

    if len(not_found) == 0:
        table = []

        grade = 0
        errors = ''

        for ex in exercises:
            res = check_exercise(2, ex)
            table.append([f"ex 2.{ex}", res[0], res[1]])
            grade += res[0]
            errors += '\n' + utils.create_error(f"ex 2.{ex}", res[2])

        errors = errors.strip()
        grade = min(grade, 100)
        report = utils.report(table)
        print(report)
        
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        
        if all:
            return grade
        else:
            utils.write_result(grade, report, 'chapter2.json')
            return grade

    else:
        utils.write_result(0, 'missing files in chapter 2: %s' % (','.join(not_found)), 'chapter2.json')



def ch3(all=False):
    exercises = ['expand', 'itoa', 'itob']
    not_found = utils.expected_files([])

    if len(not_found) == 0:
        table = []

        grade = 0
        errors = ''

        for ex in exercises:
            res = check_exercise(3, ex)
            table.append([f"ex 3.{ex}", res[0], res[1]])
            grade += res[0]
            errors += '\n' + utils.create_error(f"ex 3.{ex}", res[2])

        errors = errors.strip()
        grade = min(grade, 100)
        report = utils.report(table)
        print(report)
        
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        
        if all:
            return grade
        else:
            utils.write_result(grade, report, 'chapter3.json')
            return grade

    else:
        utils.write_result(0, 'missing files in chapter 3: %s' % (','.join(not_found)), 'chapter3.json')



def ch4(all=False):
    exercises = ['index', 'swap', 'atof']
    not_found = utils.expected_files([])

    if len(not_found) == 0:
        table = []

        grade = 0
        errors = ''

        for ex in exercises:
            res = check_exercise(4, ex)
            table.append([f"ex 4.{ex}", res[0], res[1]])
            grade += res[0]
            errors += '\n' + utils.create_error(f"ex 4.{ex}", res[2])

        errors = errors.strip()
        grade = min(grade, 100)
        report = utils.report(table)
        print(report)
        
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        
        if all:
            return grade
        else:
            utils.write_result(grade, report, 'chapter4.json')
            return grade

    else:
        utils.write_result(0, 'missing files in chapter 4: %s' % (','.join(not_found)), 'chapter4.json')



if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (BYTES, BYTES))

    parser = argparse.ArgumentParser(description="Chapter selection")
    parser.add_argument('-chapter1', action='store_true', help="Chapter 1 selected")
    parser.add_argument('-chapter2', action='store_true', help="Chapter 2 selected")
    parser.add_argument('-chapter3', action='store_true', help="Chapter 3 selected")
    parser.add_argument('-chapter4', action='store_true', help="Chapter 4 selected")
    parser.add_argument('-all', action='store_true', help="All chapters selected")

    args = parser.parse_args()

    if args.all:
        ch1_grade = ch1(all=True)
        ch2_grade = ch2(all=True)
        ch3_grade = ch3(all=True)
        ch4_grade = ch4(all=True)

        print(f"\nGrade for chapter 1: {ch1_grade}")
        print(f"\nGrade for chapter 2: {ch2_grade}")
        print(f"\nGrade for chapter 3: {ch3_grade}")
        print(f"\nGrade for chapter 4: {ch4_grade}")
    elif args.chapter1:
        grade = ch1()
        print(f"\nGrade for chapter 1: {grade}")
        print(f"\nResults saved to chapter1.json")
    elif args.chapter2:
        grade = ch2()
        print(f"\nGrade for chapter 2: {grade}")
        print(f"\nResults saved to chapter2.json")
    elif args.chapter3:
        grade = ch3()
        print(f"\nGrade for chapter 3: {grade}")
        print(f"\nResults saved to chapter3.json")
    elif args.chapter4:
        grade = ch4()
        print(f"\nGrade for chapter 4: {grade}")
        print(f"\nResults saved to chapter4.json")
    elif args.chapter5:
        print("placeholder")
    else:
        print("No chapter selected. Use -chapter1, -chapter2, -chapter3, -chapter4, or -all to selected a chapter.")
    
    utils.fix_ownership()
