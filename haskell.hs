
-- Ejercicio 1 --

fibs = 0 : 1 : [ x | x <- zipWith (+) fibs (tail(fibs)) ]

-- Ejercicio 2 --

intercambia :: Either a b -> Either b a
intercambia (Left x) = (Right x)
intercambia (Right x) = (Left x)

-- Ejercicio 3 --

join :: (a -> c) -> (b -> d) -> Either a b -> Either c d
join f g (Left a) = (Left (f a)) 
join f g (Right b) = (Right (g b))


-- Ejercicio 4 --

mapMaybe :: (a -> b) -> Maybe a -> Maybe b
mapMaybe g Nothing = Nothing
mapMaybe g (Just x) = Just (g x)

maybe1 :: b -> (a -> b) -> Maybe a -> b
maybe1 n f Nothing = n
maybe1 n f (Just x) = f x

proceso xs n m = maybe1 0 (\x -> x) ( suma_aux (mapMaybe (\x -> x) (obten_e (Just xs) n)) (mapMaybe (\x -> x) (obten_e (Just xs) m))) 

suma_aux Nothing _ = Nothing
suma_aux _ Nothing = Nothing
suma_aux (Just n) (Just m) = (Just (n+m))

obten_e (Just (x:xs)) 0 = Just x 
obten_e (Just (x:xs)) n = obten_e (Just xs) (n-1) 
obten_e _ _ = Nothing


-- Ejercicio 5 --

data ArOrd a = Vacio | Nd (ArOrd a) a (ArOrd a) deriving (Eq, Show)

insertar :: Ord a =>  a -> ArOrd a -> ArOrd a
insertar x Vacio = Nd Vacio x Vacio
insertar x (Nd izq root der)
	| x <= root =Nd (insertar x izq) root der
	| otherwise = Nd izq root (insertar x der)



eliminar :: Ord a => ArOrd a  -> a  -> ArOrd a
eliminar  Vacio x = Vacio
eliminar  (Nd izq root Vacio) x | x == root = izq
eliminar  (Nd Vacio root der) x | x == root = der
eliminar  (Nd izq root der) x
	|x < root = (Nd (eliminar izq x) root der)
	|x > root = (Nd izq root (eliminar der x ) )
	|x == root = Nd izq k (eliminar der k)
			where k = menor der


menor :: Ord a => ArOrd a -> a
menor (Nd  Vacio x _) = x
menor (Nd izq _ _)   = menor izq



list2Ar ::   [Int] -> ArOrd Int
list2Ar [] = Vacio
list2Ar  (x:xs) = insertar x (list2Ar xs)
--Nd (list2Ar (take n (quickSort xs)))  x (list2Ar (drop n ( quickSort xs)))
--where n = length xs `div` 2


ar2List :: ArOrd Int -> [Int]
ar2List Vacio = []
ar2List (Nd izq root der) =  ar2List izq ++ [root] ++ ar2List der


elem1::Ord a => ArOrd a -> a -> Bool
elem1 Vacio x = False
elem1 (Nd izq root der) x | root == x = True
			| x < root = elem1 izq x
			| x > root = elem1 der x


type Dicc = ArOrd (String,String)


traducir :: [String] -> Dicc -> [String]
traducir [] _ = []
traducir  (x:xs)  dicc = let t = buscaTraduccion x dicc in (t:traducir xs dicc)


buscaTraduccion x (Nd izq r der) | fst(r) == x = snd(r)
								 | x < fst(r) = buscaTraduccion x izq
								 | otherwise = buscaTraduccion x der


quickSort::Ord a=>[a]->[a]
quickSort [] = []
quickSort (x:xs) = quickSort(menores) ++ [x] ++ quickSort(mayores) where
	menores = [y | y <-xs, y < x]
	mayores = [z | z <-xs, z >= x]




-- Ejercicio 6 --


data  Cola a = Vacia | C ([a],[a]) deriving (Show, Eq)


vacia :: Cola a
vacia  = C ([],[])

-- inserta al final de la cola
insertaUltimo :: a -> Cola a -> Cola a
insertaUltimo y (C (xs,ys)) = C (normaliza (xs,y:ys))


insertaPrimero :: a -> Cola a -> Cola a
insertaPrimero y (C (xs,ys)) = C (normaliza (y:xs,ys))


-- funcion que se ocupa para que la primera lista no quede vacia
normaliza :: ([a],[a]) -> ([a],[a])
normaliza ([], ys) = (reverse ys, [])
normaliza p        = p

-- regresa el primer elemento de la cola pero no lo elimina
primero  :: Cola a -> a
primero (C (x:xs,ys)) = x
primero _             = error "primero: cola vacia"



ultimo  :: Cola a -> a
ultimo (C (xs,y:ys)) = y
ultimo (C (x:xs,[]))  = x
ultimo _ =	error "ultimo: cola vacia"




--regresa la cola sin el primer elemento
restoPrimero  :: Cola a -> Cola a
restoPrimero (C ([],[]))   = error "restoPrimero: cola vacia"
restoPrimero (C (x:xs,ys)) = C (normaliza (xs,ys))


restoUltimo :: Cola a -> Cola a
restoUltimo (C ([],[]))   = error "restoUltimo: cola vacia"
restoUltimo (C (xs,y:ys)) = C (normaliza (xs,ys))

-- Revis a si la cola esta vacia o no
esVacia :: Cola a -> Bool
esVacia (C (xs,_)) = null xs

-- Verific aque una cola sea valida para que la primera lista
-- nunca quede vacia
valida:: Cola a -> Bool
valida (C (xs,ys)) = not (null xs) || null ys



-- Ejercicio 7 --

leeEntero = do 
			putStr "Escribe un numero: "
			y <- getLine
			let n = read y :: Int in pide n 0


pide 0 suma = do
				putStr "La suma es: "
				putStrLn (show suma)
				return ()
pide n suma = do
				putStr "Numero "
				putStr (show n)
				putStr " = "
				y <- getLine
				let s = read y :: Int in pide (n-1) (suma + s)	



-- Ejercicio 8 --

runIO :: [IO a] -> IO [a]

runIO [] = return []
runIO (x:xs) = do
				y <- x
				ys <- runIO xs
				return (y:ys)


-- Ejercicio 9 --

forIO :: [a] -> (a -> IO ()) -> IO ()

forIO [] f = return ()
forIO (x:xs) f = do 
					f x
					forIO xs f




-- Ejemplo de ejercicio 9 -- 

fact 0 = 1
fact n = n * (fact (n-1))

prog :: IO()
prog = forIO [1..5] acc
		where acc i = do
						putStr "El factorial de "
						putStr (show i)
						putStr " es "
						putStrLn (show (fact i))


-- Ejercicio 10 --

when :: Bool -> IO a -> IO ()
when b acc = do
				if b then do { y <- acc; return () }
					else return ()

