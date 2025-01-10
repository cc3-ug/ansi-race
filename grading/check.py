import utils
import resource
import subprocess
import argparse

# 195 MiB of memory
BYTES = 195 * 1024 * 1024

ch1_ex =  ['ex-1.8.c']
ch1_in =  ['input.test']
ch1_out = ['ex108.expected']

def check_ex1(index):
    try:
        print('index: ', index)

        # compile
        task = utils.compile(target='./ch1/' + ch1_ex[index])
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        
        # run test
        task = utils.run_program(command='cat ./ch1/' + ch1_in[index] + ' | ./a.out')
        if task.returncode != 0:
            print( task.stderr.decode().strip() )
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        
        # output
        output = task.stdout.decode().strip()
        f = open('./ch1/' + ch1_out[index], 'r')
        expected = f.read().strip()
        f.close()

        if output == expected:
            return (9.1, utils.passed(), '')
        else:
            return (0, utils.failed('Error in ex 1.8'), '')
    except subprocess.TimeoutExpired:
        return(0, utils.failed('timeout'), '')
    except Exception as e:
        print(e)
        return(0, utils.failed('some other error ocurred'), '')

def check_ex108():
    try:
        # compile
        task = utils.compile(target='./ch1/ex-1.8.c')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        
        # run test
        task = utils.run_program(command='cat ./ch1/input.test | ./a.out')
        if task.returncode != 0:
            print( task.stderr.decode().strip() )
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        
        # output
        output = task.stdout.decode().strip()
        f = open('./ch1/ex108.expected', 'r')
        expected = f.read().strip()
        f.close()

        if output == expected:
            return (9.1, utils.passed(), '')
        else:
            return (0, utils.failed('Error in ex 1.8'), '')
    except subprocess.TimeoutExpired:
        return(0, utils.failed('timeout'), '')
    except Exception as e:
        print(e)
        return(0, utils.failed('some other error ocurred'), '')





def ch1(all=False):
    not_found = utils.expected_files(['./ch1/ex-1.8.c', './ch1/input.test'])

    if len(not_found) == 0:
        table = []

        ex108 = check_ex1(0)
        table.append(['ex 1.8', ex108[0], ex108[1]])

        grade = 0
        grade += ex108[0]

        errors = ''
        errors += '\n' + utils.create_error('ex 1.8', ex108[2])

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

    else:
        utils.write_result(0, 'missing files in chapter 1: %s' % (','.join(not_found)), 'chapter1.json')





if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (BYTES, BYTES))

    parser = argparse.ArgumentParser(description="Chapter selection")
    parser.add_argument('-chapter1', action='store_true', help="Chapter 1 selected")
    parser.add_argument('-chapter2', action='store_true', help="Chapter 2 selected")
    parser.add_argument('-chapter3', action='store_true', help="Chapter 3 selected")
    parser.add_argument('-chapter4', action='store_true', help="Chapter 4 selected")
    parser.add_argument('-chapter5', action='store_true', help="Chapter 5 selected")
    parser.add_argument('-all', action='store_true', help="All chapters selected")

    args = parser.parse_args()

    if args.all:
        ch1_grade = ch1(all=True)
        '''
        ch2_grade = ch2(all=True)
        ch3_grade = ch3(all=True)
        ch4_grade = ch4(all=True)
        ch5_grade = ch5(all=True)
        '''

        print(ch1_grade)
    elif args.chapter1:
        print("placeholder")
    elif args.chapter2:
        print("placeholder")
    elif args.chapter3:
        print("placeholder")
    elif args.chapter4:
        print("placeholder")
    elif args.chapter5:
        print("placeholder")
    else:
        print("No chapter selected. Use -chapter1, -chapter2, -chapter3, -chapter4, -chapter5, or -all to selected a chapter.")
    
    utils.fix_ownership()
