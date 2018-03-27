# Install Microsoft .Net Core SDK -2.1.101

The following were installed at C:\Program Files\dotnet
* .NET Core SDK 2.1.101
* .NET Core Runtime 2.0.6
*  Runtime Package Store

Resources
* [Core Documentation](https://aka.ms/dotnet-docs)
* [SDK Documentation](https://aka.ms/dotnet-cli-docs)
* [Release Notes](https://aka.ms/20-p2-rel-notes)
* [Tutorials](https://aka.ms/dotnet-tutorials)

# First Console App

    # Create Proj Dir From Tempplate
    mkdir testconsole
    cd testconsole
    dotnet new console -o testconsole
    
    # Start the program
    cd testconsole
    code Program.cs
    dotnet run

# Web App

    # Create Proj Dir From Template
    mkdir testweb
    cd testweb
    
    # start the porgam
    dotnet new web
    dotnet run
```    
Hosting environment: Production
Content root path: C:\logan\test\DotNet\testweb
Now listening on: http://localhost:5000
Application started. Press Ctrl+C to shut down.
```

# Razor Pages Web App (EF Model=>DB)

[Razor Pages web app](https://docs.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/)


    dotnet new razor -o RazorPagesMovie
    cd RazorPagesMovie
    dotnet run

    # 1. VSC->File->Open Folder->Debug(Start without debuging Ctrl-F5)

    # 2. Add a data model (a folder named Models).
    #  Add a class named Movie.cs.
    #  Add a database context class named MovieContext.cs

    # 3. Add a database connection string
```
  "ConnectionStrings": {
    "MovieContext": "Server=TORFN-L812;Initial Catalog=MovieDB;Persist Security Info=False;User ID=sa;Password=MySecret;MultipleActiveResultSets=True;"
  }
```
    # 4. Register the database context with the dependency injection container in the Startup.cs file.

```
using RazorPagesMovie.Models;
using Microsoft.EntityFrameworkCore;
...
public void ConfigureServices(IServiceCollection services)
{
    // requires 
...
    services.AddDbContext<MovieContext>(options =>
    options.UseSqlServer(Configuration.GetConnectionString("MovieContext")));
...
    services.AddMvc();
}
```
    # 5. Add Tool Reference RazorPagesMovie.csproj file.
```
DotNetCliToolReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet" Version="2.0.1" />
```
    # 6 Make sure save and close the folder on VSC before scaffold the database

    # 7 Add scaffold tooling

    dotnet add package 
    dotnet restore
    
    # 8 Perform EF migration Add package
    # 
    dotnet ef migrations add InitialCreate
```

PS C:\logan\test\DotNet\RazorPagesMovie> dir .\Migrations\
...

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        3/26/2018  12:11 PM           1282 20180326161114_InitialCreate.cs
-a----        3/26/2018  12:11 PM           1425 20180326161114_InitialCreate.Designer.cs
-a----        3/26/2018  12:11 PM           1398 MovieContextModelSnapshot.cs
```
    # 9 Run ef package InitialCreate
    dotnet ef database update

```
info: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[0]
      User profile is available. Using 'C:\Users\logan.chen\AppData\Local\ASP.NET\DataProtection-Keys' as key repository and Windows DPAPI to encrypt keys at rest.
info: Microsoft.EntityFrameworkCore.Infrastructure[10403]
      Entity Framework Core 2.0.2-rtm-10011 initialized 'MovieContext' using provider 'Microsoft.EntityFrameworkCore.SqlServer' with options: None
info: Microsoft.EntityFrameworkCore.Database.Command[20101]
      Executed DbCommand (743ms) [Parameters=[], CommandType='Text', CommandTimeout='60']
      CREATE DATABASE [MovieDB];
info: Microsoft.EntityFrameworkCore.Database.Command[20101]
      Executed DbCommand (199ms) [Parameters=[], CommandType='Text', CommandTimeout='60']
      IF SERVERPROPERTY('EngineEdition') <> 5 EXEC(N'ALTER DATABASE [MovieDB] SET READ_COMMITTED_SNAPSHOT ON;');
info: Microsoft.EntityFrameworkCore.Database.Command[20101]
      Executed DbCommand (6ms) [Parameters=[], CommandType='Text', CommandTimeout='30']
      CREATE TABLE [__EFMigrationsHistory] (
          [MigrationId] nvarchar(150) NOT NULL,
          [ProductVersion] nvarchar(32) NOT NULL,
          CONSTRAINT [PK___EFMigrationsHistory] PRIMARY KEY ([MigrationId])
      );
info: Microsoft.EntityFrameworkCore.Database.Command[20101]
      Executed DbCommand (4ms) [Parameters=[], CommandType='Text', CommandTimeout='30']
      SELECT OBJECT_ID(N'__EFMigrationsHistory');
info: Microsoft.EntityFrameworkCore.Database.Command[20101]
      Executed DbCommand (1ms) [Parameters=[], CommandType='Text', CommandTimeout='30']
      SELECT [MigrationId], [ProductVersion]
      FROM [__EFMigrationsHistory]
      ORDER BY [MigrationId];
info: Microsoft.EntityFrameworkCore.Migrations[20402]
      Applying migration '20180326162819_InitialCreate'.
Applying migration '20180326162819_InitialCreate'.
info: Microsoft.EntityFrameworkCore.Database.Command[20101]
      Executed DbCommand (2ms) [Parameters=[], CommandType='Text', CommandTimeout='30']
      CREATE TABLE [Movie] (
          [ID] int NOT NULL IDENTITY,
          [Genre] nvarchar(max) NULL,
          [Price] decimal(18, 2) NOT NULL,
          [ReleaseDate] datetime2 NOT NULL,
          [Title] nvarchar(max) NULL,
          CONSTRAINT [PK_Movie] PRIMARY KEY ([ID])
      );
Done.
info: Microsoft.EntityFrameworkCore.Database.Command[20101]
      Executed DbCommand (2ms) [Parameters=[], CommandType='Text', CommandTimeout='30']
      INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
      VALUES (N'20180326162819_InitialCreate', N'2.0.2-rtm-10011');
```      
      # 10 Generate Pages (Insert / Edit / Delete etc)
      dotnet aspnet-codegenerator razorpage -m Movie -dc MovieContext -udl -outDir Pages\Movies --referenceScriptLibraries

```
Building project ...
Finding the generator 'razorpage'...
Running the generator 'razorpage'...
Attempting to compile the application in memory.
Attempting to figure out the EntityFramework metadata for the model and DbContext: 'Movie'
info: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[0]
      User profile is available. Using 'C:\Users\logan.chen\AppData\Local\ASP.NET\DataProtection-Keys' as key repository and Windows DPAPI to encrypt keys at rest.
info: Microsoft.EntityFrameworkCore.Infrastructure[10403]
      Entity Framework Core 2.0.2-rtm-10011 initialized 'MovieContext' using provider 'Microsoft.EntityFrameworkCore.SqlServer' with options: None
Added Razor Page : \Pages\Movies\Create.cshtml
Added PageModel : \Pages\Movies\Create.cshtml.cs
Added Razor Page : \Pages\Movies\Edit.cshtml
Added PageModel : \Pages\Movies\Edit.cshtml.cs
Added Razor Page : \Pages\Movies\Details.cshtml
Added PageModel : \Pages\Movies\Details.cshtml.cs
Added Razor Page : \Pages\Movies\Delete.cshtml
Added PageModel : \Pages\Movies\Delete.cshtml.cs
Added Razor Page : \Pages\Movies\Index.cshtml
Added PageModel : \Pages\Movies\Index.cshtml.cs
RunTime 00:00:21.59
```
    # 11 Start the program
    dotnet run
```
Hosting environment: Production
Content root path: C:\logan\test\DotNet\RazorPagesMovie
Now listening on: http://localhost:5000
Application started. Press Ctrl+C to shut down.

http://localhost:5000/Movies
```
     # 11 How to listen to non localhost request

Set the port in the Main of the application where the new WebHostBuilder is created and configured. 
Just add .UseUrls() method like in the sample below

    public static void Main(string[] args)
    {
        var host = new WebHostBuilder()
            .UseUrls("http://*:5000/")
            .UseKestrel()
            .UseContentRoot(Directory.GetCurrentDirectory())
            .UseIISIntegration()
            .UseStartup<Startup>()
            .Build();

        host.Run();
    }

something like

    public static IWebHost BuildWebHost(string[] args) =>
            WebHost.CreateDefaultBuilder(args)
                .UseUrls("http://*:5000/")
                .UseStartup<Startup>()
                .Build();
    }


    # 12 Restart
    dotnet run
```
Hosting environment: Production
Content root path: C:\logan\test\DotNet\RazorPagesMovie
Now listening on: http://[::]:5000
Application started. Press Ctrl+C to shut down.

```
    # 13 Seed the database
   [Detail Link](https://docs.microsoft.com/en-us/aspnet/core/tutorials/razor-pages-vsc/sql)
   
    # Add SeedData.cs in Models
    # Add the seed initializer in main()
    # delete from Movie in ms sql database
    dotnet run


# Web App (Reversed From DB to EF Model)
[Getting Started with EF Core on ASP.NET Core with an Existing Database](<https://docs.microsoft.com/en-us/ef/core/get-started/aspnetcore/existing-db>)

Follow MVC design pattern, reverse engineering to create an Entity Framework model based on an existing database.

    #1.Create project dirs from template (MVC)
    dotnet new mvc -o testmvcweb
    
    #2.To use EF Core, install the package for the database provider(s) you want to target
    dotnet add testmvcweb package Microsoft.EntityFrameworkCore.SqlServer
    
    #3.install the EF tools package
    dotnet add testmvcweb package Microsoft.EntityFrameworkCore.Tools 
    
    #4.install ASP.NET Core Scaffolding tools package
    dotnet add testmvcweb package Microsoft.VisualStudio.Web.CodeGeneration.Design
    
    #5.Check porject.json and let CliTool exposed
```
<DotNetCliToolReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet"  Version="2.0.0" />
```    
          
[EF Core .NET Command-line Tools](<https://docs.microsoft.com/en-us/ef/core/miscellaneous/cli/dotnet>)

    #6.Reverse engineer your EF model from database
    # For more commands from above link
    
    dotnet ef -h
    
    # This will generate dbcontext <Table>.cs under Models
    dotnet ef dbcontext scaffold "Server=TORFN-L812;Initial Catalog=Blogging;Persist Security Info=False;User ID=sa;Password=Xmas2017;MultipleActiveResultSets=False;" Microsoft.EntityFrameworkCore.SqlServer -o Models -f -c BloggingContext --verbose
    
    dir .\Models
    
    #7. Register your context with dependency injection
    # Models\BloggingContext.cs: 
    #    => Delete method OnConfiguring(...) 
    #    <= Add the following method allow configuration to be passed into the context by dependency injection
    #
```
         public BloggingContext(DbContextOptions<BloggingContext> options)
            : base(options)
        { }
```
 
    #8. Register and configure your context in Startup.cs
    # in Startup.cs, add the references:
```    
    using testmvcweb.Models;
    using Microsoft.EntityFrameworkCore;
    
    # at ConfigureServices(...)
    #
    
        public void ConfigureServices(IServiceCollection services)
        {
 

        services.AddMvc();
    
        var connection = @"Server=TORFN-L812;Initial Catalog=Blogging;Persist Security Info=False;User ID=sa;Password=MySecret;";
        services.AddDbContext<BloggingContext>(options => options.UseSqlServer(connection));
            
        }
``` 
    # 9 Generate Pages (Insert / Edit / Delete etc)
    cd ..\
```
    # 9.1. Install package for the tool
    dotnet add testmvcweb package Microsoft.VisualStudio.Web.CodeGeneration.Design
    cd .\testmvcweb\
    dotnet restore
    # 
    dotnet.exe aspnet-codegenerator --help
    dotnet.exe aspnet-codegenerator controller --help
```
    #
    # 9.2. Generate Controller / Views for Entity Blog
    #
    dotnet aspnet-codegenerator controller -p .\ -name BlogController -m testmvcweb.Models.Blog -dc BloggingContext -outDir .\Controllers -f
```
Building project ...
Finding the generator 'controller'...
Running the generator 'controller'...
Attempting to compile the application in memory.
Attempting to figure out the EntityFramework metadata for the model and DbContext: 'Blog'
info: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[0]
      User profile is available. Using 'C:\Users\logan.chen\AppData\Local\ASP.NET\DataProtection-Keys' as key repository and Windows DPAPI to encrypt keys at rest.
info: Microsoft.EntityFrameworkCore.Infrastructure[10403]
      Entity Framework Core 2.0.2-rtm-10011 initialized 'BloggingContext' using provider 'Microsoft.EntityFrameworkCore.SqlServer' with options: None
Added Controller : '\.\Controllers\BlogController.cs'.
Added View : \Views\Blog\Create.cshtml
Added View : \Views\Blog\Edit.cshtml
Added View : \Views\Blog\Details.cshtml
Added View : \Views\Blog\Delete.cshtml
Added View : \Views\Blog\Index.cshtml
RunTime 00:00:17.24
```
     #
     # 9.3. Generate Controller / Views for Entity Post
     #
     dotnet aspnet-codegenerator controller -p .\ -name PostController -m testmvcweb.Models.Post -dc BloggingContext -outDir .\Controllers -f
```
Building project ...
Finding the generator 'controller'...
Running the generator 'controller'...
Attempting to compile the application in memory.
Attempting to figure out the EntityFramework metadata for the model and DbContext: 'Post'
info: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[0]
      User profile is available. Using 'C:\Users\logan.chen\AppData\Local\ASP.NET\DataProtection-Keys' as key repository and Windows DPAPI to encrypt keys at rest.
info: Microsoft.EntityFrameworkCore.Infrastructure[10403]
      Entity Framework Core 2.0.2-rtm-10011 initialized 'BloggingContext' using provider 'Microsoft.EntityFrameworkCore.SqlServer' with options: None
Added Controller : '\.\Controllers\PostController.cs'.
Added View : \Views\Post\Create.cshtml
Added View : \Views\Post\Edit.cshtml
Added View : \Views\Post\Details.cshtml
Added View : \Views\Post\Delete.cshtml
Added View : \Views\Post\Index.cshtml
RunTime 00:00:19.03
```
    #10. Start the site
    dotnet run
    
    # browser=> http://localhost:5000/Blog
    # browser=> http://localhost:5000/Post
    

# References

[Database Providers](https://docs.microsoft.com/en-us/ef/core/providers/index)

[Introduction to Entity Framework](<https://msdn.microsoft.com/en-us/library/aa937723(v=vs.113).aspx>)