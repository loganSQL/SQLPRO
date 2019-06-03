USE [msdb]
GO

/****** Object:  StoredProcedure [dbo].[sendOutputEmail]    Script Date: 2019-06-03 12:05:21 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE procedure [dbo].[sendOutputEmail] 
(@job_name varchar(255), @outfile varchar(1024), @emails varchar(1024))
as
select @job_name= @job_name+' Daily Run At '+	CONVERT(VARCHAR(24), GETDATE(), 113)
EXEC msdb.dbo.sp_send_dbmail
@profile_name = 'sqladmin',
@recipients = @emails,
@body = 'The result has been attached.',
@file_attachments = @outfile,
@subject = 	@job_name ;
GO
