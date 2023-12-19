import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()


def main():
    name = ''
    job = ''
    salary_impost_ir = 0
    salary_impost_inss = 0
    salary = 0
    try:
        name = input('Digite seu nome completo: ')
        job = input('Digite seu cargo atual: ')
        salary = float(input('Digite seu salário bruto em Reais: ').replace(",", "."))

    except TypeError:
        print('Digite um valor válido!')
        main()

    # if relacionado ao imposto de renda
    if 2826.65 > salary > 2112.00:
        salary_impost_ir = 7.5
    elif 3751.05 > salary > 2826.66:
        salary_impost_ir = 15
    elif 4664.67 > salary > 3751.06:
        salary_impost_ir = 22.50
    elif 4664.68 < salary:
        salary_impost_ir = 27.50
    # fim do if do imposto de renda

    # if relacionado ao inss
    if salary <= 1320.00:
        salary_impost_inss = 7.50
    elif 2571.29 > salary > 1320.00:
        salary_impost_inss = 9.00
    elif 3856.94 > salary > 2571.30:
        salary_impost_inss = 12.00
    elif 7507.49 > salary > 3856.95:
        salary_impost_inss = 14.00
    elif 7507.49 < salary:
        salary_impost_inss = 14.00

    def calculate_tax(a, b, c):
        (a / 100) * (100 - (b + c))

    salary_impost_fgts = (salary * 8) / 100
    data_show_ir = (salary * salary_impost_ir) / 100
    data_show_inss = (salary * salary_impost_inss) / 100

    print(' ')
    print('Nome: ', name)
    print('Cargo: ', job)
    print(f'-------------------------------Salário bruto: {salary}')
    print(' ')
    print(f'------------imposto de renda: {salary_impost_ir}% -{data_show_ir}')
    print(f'------------Desconto de INSS: {salary_impost_inss}%-{data_show_inss}')
    print(f'------------FGTS: R${salary_impost_fgts}')
    print(' ')
    print(
        f'-------------------------------Salário líquido após desconto de imposto de renda: '
        f'{calculate_tax(salary, salary_impost_ir, salary_impost_inss)}\n ')

    text_name = ap.text.TextFragment(f"Nome: {name}")
    text_job = ap.text.TextFragment(f"Cargo: {job}")
    text_reductions = ap.text.TextFragment(f"-------------------------------Salário bruto: {salary} \n"
                                           f"\n"
                                           f"------------Imposto de renda: {salary_impost_ir}%:  -{data_show_ir} \n"
                                           f"------------Desconto de INSS: {salary_impost_inss}%: -{data_show_inss} \n"
                                           f"------------FGTS: R${salary_impost_fgts} \n"
                                           f"-------------------------------Salário líquido após "
                                           f"desconto de imposto de renda: "
                                           f"{calculate_tax(salary, salary_impost_ir, salary_impost_inss)}\n ")
    page.paragraphs.add(text_name)
    page.paragraphs.add(text_job)
    page.paragraphs.add(text_reductions)

    document.save(f"folha de pagamento {name}.pdf")


if __name__ == '__main__':
    main()
