Feature: CSV File Comparison

  Scenario Outline: CSV Comparison
    Given <InputCSV> is present
    When Dev Src Code is run with <InputCSV> and <OutputCSV>
    Then <OutputCSV> is generated
    And <OutputCSV> Contents are same as <ExpOutputCSV> file

    Examples:
      | InputCSV     | ExpOutputCSV | OutputCSV |
      | /home/saurabh/Documents/Automation/CSVCompare/src/Input1.csv    | /home/saurabh/Documents/Automation/CSVCompare/src/ExpOutput1.csv | /home/saurabh/Documents/Automation/CSVCompare/src/Output1.csv |
      | /home/saurabh/Documents/Automation/CSVCompare/src/Input2.csv    | /home/saurabh/Documents/Automation/CSVCompare/src/ExpOutput2.csv | /home/saurabh/Documents/Automation/CSVCompare/src/Output2.csv |
