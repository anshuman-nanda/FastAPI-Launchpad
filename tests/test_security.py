"""
Test security utilities.
"""

import pytest

from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    get_password_hash,
    verify_password,
)


def test_password_hashing():
    """Test password hashing and verification."""
    password = "test_password_123"
    hashed = get_password_hash(password)
    
    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("wrong_password", hashed)


def test_access_token_creation():
    """Test JWT access token creation and decoding."""
    data = {"sub": "user123", "username": "testuser"}
    token = create_access_token(data)
    
    assert token is not None
    assert isinstance(token, str)
    
    decoded = decode_token(token)
    assert decoded is not None
    assert decoded["sub"] == "user123"
    assert decoded["username"] == "testuser"
    assert "exp" in decoded


def test_refresh_token_creation():
    """Test JWT refresh token creation and decoding."""
    data = {"sub": "user123"}
    token = create_refresh_token(data)
    
    assert token is not None
    assert isinstance(token, str)
    
    decoded = decode_token(token)
    assert decoded is not None
    assert decoded["sub"] == "user123"
    assert decoded["type"] == "refresh"
    assert "exp" in decoded


def test_invalid_token_decode():
    """Test decoding invalid token."""
    invalid_token = "invalid.token.here"
    decoded = decode_token(invalid_token)
    assert decoded is None
