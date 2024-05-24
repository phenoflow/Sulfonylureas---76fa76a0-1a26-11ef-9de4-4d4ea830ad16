# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"32","system":"gprdproduct"},{"code":"34932","system":"gprdproduct"},{"code":"45215","system":"gprdproduct"},{"code":"34399","system":"gprdproduct"},{"code":"36856","system":"gprdproduct"},{"code":"42790","system":"gprdproduct"},{"code":"29939","system":"gprdproduct"},{"code":"43065","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('sulfonylureas-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["sulfonylureas-gliclazide---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["sulfonylureas-gliclazide---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["sulfonylureas-gliclazide---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
