USE [BonosAPP]
GO

/** Object:  Table [dbo].[Bono]    Script Date: 16/4/2020 19:14:29 **/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Bono](
	[id_bono] [int] NULL,
	[id_usuario] [int] NULL,
	[flavor] [varchar](50) NULL,
	[isin] [varchar](50) NULL,
	[maturity] [date] NULL
) ON [PRIMARY]
GO