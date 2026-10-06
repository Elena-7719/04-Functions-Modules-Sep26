import re  # Для поиска по марке без учета регистра

def show_all(clients):
    """1. Выводит всех клиентов в удобном формате таблицы."""
    print(f"\n{'ID':<4} | {'ФИО Клиента':<18} | {'Марка':<12} | {'Год':<5} | {'Стоимость':<10}")
    print("-" * 60)
    for client in clients:
        print(f"{client[0]:<4} | {client[1]:<18} | {client[2]:<12} | {client[3]:<5} | {client[4]:<10} руб.")

def filter_by_brand(clients, brand):
    """2. Возвращает список клиентов указанной марки автомобиля."""
    result = []
    for client in clients:
        if re.search(brand, client[2], re.IGNORECASE):
            result.append(client)
    return result

def add_service_cost(clients, index, amount):
    """3. Добавляет сумму к стоимости обслуживания клиента по индексу."""
    clients[index][4] = clients[index][4] + amount

def delete_by_index(clients, index):
    """4. Удаляет клиента по номеру (индексу) в списке."""
    del clients[index]

def get_most_expensive(clients):
    """5*. Возвращает клиента(ов) с максимальной стоимостью обслуживания."""
    max_cost = 0
    for client in clients:
        if client[4] > max_cost:
            max_cost = client[4]
            
    result = []
    for client in clients:
        if client[4] == max_cost:
            result.append(client)
    return result

def delete_older_than(clients, years):
    """6*. Удаляет старых клиентов и ВОЗВРАЩАЕТ количество удаленных."""
    current_year = 2026
    kept_clients = []
    count_before = len(clients)
    
    for client in clients:
        car_age = current_year - client[3]
        if car_age <= years:
            kept_clients.append(client)
            
    clients.clear()
    clients.extend(kept_clients)
    
    deleted_now = count_before - len(clients)
    return deleted_now

def create_delete_counter():
    """7. Функция-замыкание для подсчета удаленных за сессию."""
    total_deleted = 0
    def count_deleted(number):
        nonlocal total_deleted
        total_deleted = total_deleted + number
        return total_deleted
    return count_deleted
