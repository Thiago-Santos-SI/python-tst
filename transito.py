seg = int(input())
ter = int(input())
qua = int(input())
qui = int(input())
sex = int(input())

total = seg + ter + qua + qui + sex
episodios = total//50
media = total/5
semana_produtiva = 5 * 24 * 60
porcentagem = (total/semana_produtiva) * 100

print(f'Você perdeu {total} min na semana (média de {media:.1f} min por dia).')
print(f'Isso significa {porcentagem:.2f}% da sua semana produtiva.')
print(f'Daria para assistir {episodios} episódio(s) de House.')


