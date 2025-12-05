
import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] =='defunkt'


@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']
    
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergii_butenko_not_exist")
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emodjis_exists(github_api):
    emojis = github_api.get_emojis()
    assert emojis["100"] == "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8"


@pytest.mark.api
def test_emodjis_not_equal(github_api):
    emojis = github_api.get_emojis()
    assert emojis["100"] != "https://github.githubassets.com/images/icons/emoji/unicode/1f522.png?v8"


@pytest.mark.api
def test_emodjis_exists_one_more(github_api):
    emojis = github_api.get_emojis()
    assert emojis["1234"] == "https://github.githubassets.com/images/icons/emoji/unicode/1f522.png?v8"

