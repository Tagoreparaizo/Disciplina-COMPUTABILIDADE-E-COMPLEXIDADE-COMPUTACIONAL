expMult :: Int -> Int -> Int
expMult _ 0 = 1
expMult base expoente = base * expMult base (expoente - 1)

logDiv :: Int -> Int -> Int
logDiv base valor
    | valor < base = 0
    | otherwise    = 1 + logDiv base (valor `div` base)

main :: IO ()
main = do
    putStrLn "--- Testando Exponenciação (expMult) ---"
    putStrLn ("2 ^ 3 = " ++ show (expMult 2 3))
    putStrLn ("5 ^ 4 = " ++ show (expMult 5 4))
    
    putStrLn "\n--- Testando Logaritmo Inteiro (logDiv) ---"
    putStrLn ("Log base 2 de 8 = " ++ show (logDiv 2 8))
    putStrLn ("Log base 10 de 1000 = " ++ show (logDiv 10 1000))