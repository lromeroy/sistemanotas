-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-03-2019 a las 22:51:32
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistemanotas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_estudiantes`
--

CREATE TABLE `datos_estudiantes` (
  `id_estudiante` int(11) NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `datos_estudiantes`
--

INSERT INTO `datos_estudiantes` (`id_estudiante`, `email`, `telefono`) VALUES
(25034065, 'joseramirez24@gmail.com', '0416-1234565'),
(25054056, 'carlosnu@gmail.com', '0416-2345216'),
(25058046, 'msalas.095@gmail.com', '0412-1959127'),
(26043052, 'pabloescobar@gmail.com', '0416-424578'),
(26625100, 'luis.ry.15@gmail.com', '0412-3530370'),
(26904942, 'perdogon@gmail.com', '0412-423450');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id`, `nombre`) VALUES
(25034065, 'Jose Ramirez'),
(25054056, 'Carlos Osorio'),
(25058046, 'Manuel Salas'),
(26043052, 'Pablo Cesar'),
(26625100, 'Luis Romero'),
(26904942, 'Pedro Gonzalez');

--
-- Disparadores `estudiantes`
--
DELIMITER $$
CREATE TRIGGER `delete_notas` AFTER DELETE ON `estudiantes` FOR EACH ROW BEGIN
	DELETE FROM notas_estudiantes WHERE old.id = id_estudiante;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `insert_notas` AFTER INSERT ON `estudiantes` FOR EACH ROW BEGIN
	insert into notas_estudiantes (id_estudiante, nota) VALUES (new.id, 0);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notas_estudiantes`
--

CREATE TABLE `notas_estudiantes` (
  `id_estudiante` int(11) NOT NULL,
  `nota` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `notas_estudiantes`
--

INSERT INTO `notas_estudiantes` (`id_estudiante`, `nota`) VALUES
(25034065, 10),
(25054056, 4),
(25058046, 1),
(26043052, 7),
(26625100, 1),
(26904942, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`id`, `nombre`, `user_id`) VALUES
(213, 'asd', 17),
(8491308, 'Crisogono Romero', 16),
(8605708, 'Carlos Marcano', 1),
(8940948, 'Kike Romero', 8),
(23204053, 'Marcos Rojas', 15),
(25058046, 'Manuel Salas', 7),
(25058049, 'Manuel Salas', 18),
(26625100, 'Luis Romero', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `email`, `password`) VALUES
(1, 'carlosmarcano@gmail.com', '1234'),
(6, 'luis.ry.15@gmail.com', 'funtrack123'),
(7, 'msalas.095@gmail.com', '1234'),
(8, 'crisjoromero@gmail.com', '1234'),
(15, 'marcosrojas@gmail.com', '1010'),
(16, 'crisjoromero@hotmail.com', '150399'),
(17, 'luis.ry.w15@gmail.com', '123'),
(18, 'kiki@ki.com', '123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos_estudiantes`
--
ALTER TABLE `datos_estudiantes`
  ADD PRIMARY KEY (`id_estudiante`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `notas_estudiantes`
--
ALTER TABLE `notas_estudiantes`
  ADD PRIMARY KEY (`id_estudiante`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
