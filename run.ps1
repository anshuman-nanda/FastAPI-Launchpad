# FastAPI Helper Script
# Usage: .\run.ps1 [command]

param([string]$Command = "help")

# Add Poetry to PATH if not found
if (-not (Get-Command poetry -ErrorAction SilentlyContinue)) {
    $env:Path += ";C:\Users\anshu\AppData\Roaming\Python\Scripts"
}

function Show-Help {
    Write-Host "`nFastAPI Helper Script" -ForegroundColor Cyan
    Write-Host "`nDocker Commands:" -ForegroundColor Yellow
    Write-Host "  up           - Start all services"
    Write-Host "  down         - Stop all services"
    Write-Host "  logs         - View logs"
    Write-Host "  rebuild      - Rebuild and restart"
    Write-Host "`nDevelopment Commands:" -ForegroundColor Yellow
    Write-Host "  start        - Start app locally"
    Write-Host "  test         - Run tests"
    Write-Host "  format       - Format code"
    Write-Host "  lint         - Lint code"
    Write-Host "`n"
}

switch ($Command.ToLower()) {
    "up" { 
        Write-Host "Starting services..." -ForegroundColor Green
        docker-compose up -d
        Write-Host "`nAPI: http://localhost:8000/docs" -ForegroundColor Cyan
    }
    "down" { 
        Write-Host "Stopping services..." -ForegroundColor Green
        docker-compose down 
    }
    "logs" { 
        docker-compose logs -f app 
    }
    "rebuild" { 
        Write-Host "Rebuilding..." -ForegroundColor Green
        docker-compose up -d --build 
    }
    "start" { 
        Write-Host "Starting locally..." -ForegroundColor Green
        poetry run uvicorn app.main:app --reload 
    }
    "test" { 
        poetry run pytest 
    }
    "format" { 
        poetry run black . 
    }
    "lint" { 
        poetry run ruff check . 
    }
    default { Show-Help }
}

