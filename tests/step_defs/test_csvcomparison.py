from pytest_bdd import given, when, then, scenario
from csv import reader
import os

@scenario('filecomp.feature', 'CSV Comparison')
def test_CSV_Comparison():
    pass


@given('<InputCSV> is present')
def Input_CSV_is_present(InputCSV):
    assert os.path.isfile(InputCSV)

@when('Dev Src Code is run with <InputCSV> and <OutputCSV>')
def Dev_Src_Code_is_run(InputCSV, OutputCSV):
    os.system('python /home/saurabh/Documents/Automation/testproject1/src/create_csv.py -i ' + InputCSV + ' -o ' + OutputCSV)
    print("Output File Generated")

@then('<OutputCSV> is generated')
def Output_CSV_is_generated(OutputCSV):
    assert os.path.isfile(OutputCSV)

@then('<OutputCSV> Contents are same as <ExpOutputCSV> file')
def Compare_Output_CSV(OutputCSV, ExpOutputCSV):
    with open(OutputCSV, 'r') as output:
        output_csv_content = reader(output)
        oplst = list(output_csv_content)
    with open(ExpOutputCSV, 'r') as expoutput:
        exp_csv_content = reader(expoutput)
        expoplst = list(exp_csv_content)
    assert oplst[0] == expoplst[0]
    oplst.sort(reverse=True)
    expoplst.sort(reverse=True)
    assert oplst == expoplst
    assert 2+3 == 5
