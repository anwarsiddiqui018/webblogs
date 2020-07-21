from tabula import read_pdf

df = read_pdf("table.pdf", multiple_tables=True)

print(df)