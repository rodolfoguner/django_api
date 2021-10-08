from validate_docbr import CPF

def valid_name(name):
    return name.isalpha()


def valid_cpf(cpf_number):
    cpf = CPF()
    return cpf.validate(cpf_number)
