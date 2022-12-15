# This script is the duplicate of pandas.ipynb. Do not run it!

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Задание 1. Работа с реальными данными
# Напишите функции read_gff и read_bed6 для чтения соответствующих форматов. Они должны возвращать датафреймы как в примере (картинка Example1), но имена колонок можно сделать любыми.

def read_gff(file):
    gff = pd.read_table(file, sep='\t', skiprows=1, names=['chromosome', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'])
    return gff

gff = read_gff('~/IB/python/Python_BI_2022/homework_5_pandas/rrna_annotation.gff')
gff.head()

def read_bed6(file):
    bed = pd.read_table(file, sep='\t', names=['chromosome', 'start', 'end', 'name', 'score', 'strand'])
    return bed

bed = read_bed6('~/IB/python/Python_BI_2022/homework_5_pandas/alignment.bed')
bed.head()

# Колонка с атрибутами несёт слишком много избыточной информации и ей не удобно пользоваться, оставьте в ней только данные о типе рРНК одной короткой строкой (16S, 23S, 5S).

gff['attributes'] = gff['attributes'].str.extract(r'(\d+S)')
gff.head()
gff['attributes'].unique()

# Сделайте таблицу, где для каждой хромосомы (на самом деле это не хромосомы, а референсные геномы) показано количество рРНК каждого типа. Постройте barplot, отображающий эти данные (картинка rRNA_barplot)

rrna_types = gff[['chromosome', 'attributes']].value_counts().to_frame().reset_index('chromosome').reset_index('attributes')
rrna_types = rrna_types.rename(columns={0: 'count'})

rrna_types['sort_att'] = rrna_types['attributes'].str.extract('(\d+)').astype(int)
rrna_types['sort_ch'] = rrna_types['chromosome'].str.extract('(\d+)').astype(int)
rrna_types = rrna_types.sort_values(by=['sort_ch', 'sort_att'], ignore_index=True)
rrna_types = rrna_types.drop(['sort_att', 'sort_ch'], axis=1)

rrna_types.head()

fig1 = sns.barplot(rrna_types, x = 'chromosome', y = 'count', hue='attributes')
fig1.set(xlabel='Sequence', ylabel='Count')
fig1.legend(title='RNA type')
fig1.set_xticklabels(fig1.get_xticklabels(), rotation=90)
plt.show()

# Далее самое интересное. Мы хотим узнать сколько рРНК в процессе сборки успешно собралось. Для этого можно воспользоваться программой bedtools intersect и пересечь эти два файла. В результате сохранятся только записи об рРНК, интервал которой перекрывался с интервалом контига в выравнивании, это означает, что это ген есть в сборке. Но забудьте про bedtools! У нас тут вообще-то пандас! Поэтому давайте получим такой же результат в нём. Выведите таблицу, содержащую исходные записи об рРНК полностью вошедших в сборку (не фрагментом), а также запись о контиге в который эта РНК попала. Итоговая таблица должна выглядеть примерно так (картинка Example2). Обратите внимание, что в один контиг может попасть несколько рРНК.

intersected = bed.merge(gff, on='chromosome', suffixes=['_x', '_y'])
intersected

# Проставляем минусы, чтобы сравнять позиции аннотаций GFF и BED: -1 для start_y и end_y от GFF, и дополнительный -1 для end от GFF, так как GFF end включает конец интервала, а BED end - нет

intersected = intersected[intersected['start_x'] <= (intersected['start_y'] - 1)][intersected['end_x'] >= intersected['end_y'] - 2]
intersected

# Задание 2. Кастомизация графиков

diff = pd.read_csv('~/IB/python/Python_BI_2022/homework_5_pandas/diffexpr_data.tsv.gz', sep='\t')
diff

diff.loc[(diff['logFC'] >= 0) & (diff['pval_corr'] >= 0.05), 'segments'] = 'ns_up'
diff.loc[(diff['logFC'] < 0) & (diff['pval_corr'] >= 0.05), 'segments'] = 'ns_down'
diff.loc[(diff['logFC'] >= 0) & (diff['pval_corr'] < 0.05), 'segments'] = 's_up'
diff.loc[(diff['logFC'] < 0) & (diff['pval_corr'] < 0.05), 'segments'] = 's_down'

sorter = ['s_down', 's_up', 'ns_down', 'ns_up']
diff['segments'] = diff['segments'].astype('category')
diff['segments'] = diff['segments'].cat.set_categories(sorter)
#diff = diff.sort_values(by=['segments'], ignore_index=True)
diff

hline_p = -(np.log10(0.05))

maxfc, minfc = max(diff['logFC']), min(diff['logFC'])
max_abs_fc = max(abs(maxfc), abs(minfc))
min_x, max_x = -(max_abs_fc) - 1, max_abs_fc + 1
print(min_x, max_x)

sup_two = diff[diff['segments'] == 's_up'].sort_values(by=['logFC'], ascending=False)[:2]
sup_two

sdown_two = diff[diff['segments'] == 's_down'].sort_values(by=['logFC'])[:2]
sdown_two

plt.rcParams['figure.figsize'] = [16, 10]

palette ={'s_down': 'C0', 's_up': 'C1', 'ns_down': 'C2', 'ns_up': 'C3'}

# 1
vol = sns.scatterplot(diff, x='logFC', y='log_pval', hue = 'segments', palette=palette, s = 20, edgecolor = None)
vol.patch.set_linewidth(15)  
vol.axhline(hline_p, color='grey', linestyle='--', linewidth=2)
vol.axvline(0, color='grey', linestyle='--', linewidth=2)
vol.text(8, 2, 'p-value = 0.05', horizontalalignment='left', size='large', color='grey', weight='semibold')

# # 2
plt.xlabel('log\u2082 (fold change)', size=20, fontstyle='italic', weight=1000)
plt.ylabel('-log\u2081\u2080 (p value corrected)', size=20, fontstyle='italic', weight=1000)
plt.title('Volcano plot', size=32, fontstyle='italic', weight=1000)
vol.minorticks_on()
plt.xticks(size=14, weight=1000)
plt.yticks(size=14, weight=1000)
vol.tick_params(width=2, length=7)
vol.tick_params(which='minor', width=2, length=3)
vol.set_xlim(min_x, max_x)
for _,s in vol.spines.items():
    s.set_linewidth(2)
    
# # 3
vol.legend(prop={'family':'DejaVu Sans', 'size': 14, 'weight': 'semibold'}, markerscale=2.0, shadow=True, labels=['Significantly downregulated', 'Significantly upregulated', 'Non-significantly downregulated', 'Non-significantly upregulated'])
# На этом шаге при добавлении labels почему-то первый маркер в легенде становится меньше остальных... Почему - так и не поняла...

# 4
vol.annotate(sup_two['Sample'].iloc[0], 
            xy=(sup_two['logFC'].iloc[0], sup_two['log_pval'].iloc[0] + 1),
            xytext=(sup_two['logFC'].iloc[0] - 0.5, sup_two['log_pval'].iloc[0] + 10), 
            arrowprops=dict(width=3, edgecolor='black', facecolor='red'), weight=700)
vol.annotate(sup_two['Sample'].iloc[1], 
            xy=(sup_two['logFC'].iloc[1], sup_two['log_pval'].iloc[1] + 1),
            xytext=(sup_two['logFC'].iloc[1] - 0.5, sup_two['log_pval'].iloc[1] + 10), 
            arrowprops=dict(width=3, edgecolor='black', facecolor='red'), weight=700)
vol.annotate(sdown_two['Sample'].iloc[0], 
            xy=(sdown_two['logFC'].iloc[0], sdown_two['log_pval'].iloc[0] + 1),
            xytext=(sdown_two['logFC'].iloc[0] - 0.5, sdown_two['log_pval'].iloc[0] + 10), 
            arrowprops=dict(width=3, edgecolor='black', facecolor='red'), weight=700)
vol.annotate(sdown_two['Sample'].iloc[1], 
            xy=(sdown_two['logFC'].iloc[1], sdown_two['log_pval'].iloc[1] + 1),
            xytext=(sdown_two['logFC'].iloc[1] - 0.5, sdown_two['log_pval'].iloc[1] + 10), 
            arrowprops=dict(width=3, edgecolor='black', facecolor='red'), weight=700);

