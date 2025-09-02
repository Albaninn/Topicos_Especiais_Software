# --- Constantes Globais ---
DESCONTO_PADRAO = 0.105
VALOR_MINIMO_DESCONTO = 100.00

desconto_padrao_da_loja =  lambda subtotal: (
    
    (subtotal * DESCONTO_PADRAO,
     f"Desconto ({DESCONTO_PADRAO * 100:.1f}%): R$ {subtotal * DESCONTO_PADRAO:.2f}")

    if subtotal > VALOR_MINIMO_DESCONTO
    else ( 0,f"Compras acima de R$ {VALOR_MINIMO_DESCONTO:.2f} recebem desconto.")
)