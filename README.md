
# Bank Customer Executive Dashboard (Power BI)

Интерактивный дашборд для анализа клиентского портфеля банка, отслеживания оттока (Churn Rate) и выявления факторов риска.

> **Пометка про данные:** Данные в этом пет-проекте были искусственно сгенерированы в целях полного контроля над датасетом для высокого качества обучения.

##  Стек
Power BI Desktop, DAX, Power Query, Python (Pandas/NumPy для генерации данных).

## Ключевые DAX-метрики
* **Total Customers:** `COUNTROWS('bank_analytics_data')`
* **Churned Customers:** `CALCULATE(COUNTROWS('bank_analytics_data'), 'bank_analytics_data'[Exited] = 1)`
* **Churn Rate:** `DIVIDE([Churned Customers], [Total Customers], 0)`
* **Total Balance:** `SUM('bank_analytics_data'[Balance])`

## Выводы аналитики
1. **Продуктовая перегрузка:** Клиенты с 3 и 4 подключенными продуктами демонстрируют аномально высокий отток (~75-80%).
2. **Возрастной фактор:** Риск оттока существенно возрастает в возрастной группе 45+.
3. **Фактор активности:** Неактивные участники (`Is_Active_Member = 0`) составляют основную часть уходящего портфеля.

<img width="1317" height="744" alt="Screenshot 2026-08-24 001623" src="https://github.com/user-attachments/assets/34c98227-1594-4d06-b3a9-e2f5aac16304" />
