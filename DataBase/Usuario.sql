USE [BonosAPP]
GO

/** Object:  Table [dbo].[Usuario]    Script Date: 16/4/2020 19:15:19 **/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Usuario](
	[id_usuario] [int] NULL,
	[id_rol] [int] NULL,
	[nombre] [varchar](50) NULL,
	[password] [varchar](50) NULL
) ON [PRIMARY]
GO