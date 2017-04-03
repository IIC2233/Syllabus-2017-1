def dividir(num, den):
    try:
        return float(num) / float(den)
    except (ZeroDivisionError) as err:
        print('Error: {}'.format(err))
        print('El denominador debe ser distinto de 0')


if __name__ == '__main__':
    dividir(1, 0)
