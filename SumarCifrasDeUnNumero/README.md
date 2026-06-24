# Suma de Cifras de un Número

Trabajo Práctico de Lógica - Tema 6

## Descripción

Programa educativo que calcula la suma de las cifras de un número entero no negativo. El proyecto forma parte del Trabajo Práctico (TP) de Lógica para la Comisión 9 del año 2026.

## Características

- ✅ Calcula la suma de dígitos de un número entero
- ✅ Validación robusta de entrada del usuario
- ✅ Manejo completo de errores y excepciones
- ✅ Rechaza números negativos
- ✅ Rechaza entrada con signo `+` explícito
- ✅ Control de tipo de datos (solo acepta enteros)

## Requisitos

- Python 3.6 o superior

## Cómo usar

1. Ejecutar el programa:
```bash
python tp_logica.py
```

2. Ingresar un número entero no negativo cuando se solicite:
```
Ingresá un número entero mayor o igual a cero: 
```

3. El programa mostrará la suma de sus cifras:
```
La suma de las cifras de 12345 es: 15
```

## Ejemplos

```
Entrada: 0      → Suma: 0
Entrada: 42     → Suma: 6
Entrada: 123    → Suma: 6
Entrada: 9999   → Suma: 36
```

## Validaciones

El programa valida:
- Que la entrada sea un número entero válido
- Que el número no sea negativo
- Que no contenga signo `+` explícito
- Que el parámetro sea de tipo entero dentro de la función

## Estructura del código

- **Función `resolver(n)`**: Calcula la suma de cifras usando un algoritmo iterativo
  - Recibe: un número entero no negativo
  - Retorna: la suma de sus dígitos
  - Valida: tipo de dato y rango de valores

- **Programa principal**: Gestiona la entrada del usuario y maneja excepciones

## Autor

Paulo Orsini  
Comisión 9 - 2026
