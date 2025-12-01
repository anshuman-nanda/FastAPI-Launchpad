## FastAPI Quick Reference

### Start Everything
```powershell
docker-compose up -d
# Visit: http://localhost:8000/docs
```

### Common Commands
```powershell
.\run.ps1 up        # Start all services
.\run.ps1 down      # Stop all services
.\run.ps1 logs      # View logs
.\run.ps1 rebuild   # Rebuild after changes
.\run.ps1 test      # Run tests
```

### Useful Docker Commands
```powershell
docker-compose ps              # Check status
docker-compose logs -f app     # Follow app logs
docker-compose restart app     # Restart app
docker-compose exec app bash   # Shell into container
docker-compose down -v         # Remove everything + data
```

### Access Services
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- PostgreSQL: localhost:5432
- Redis: localhost:6379

That's all you need! 🚀
