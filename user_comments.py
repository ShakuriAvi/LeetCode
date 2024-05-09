from requests import request
from typing import Dict


class Solution:
    user_posts = {
        1: [
            {
                "post_id": 1,
                "created_at": "2024-04-22T10:00:00Z",
                "other_field": "value"
            },
            {
                "post_id": 2,
                "created_at": "2024-04-21T15:30:00Z",
                "other_field": "value"
            },
            {
                "post_id": 3,
                "created_at": "2024-04-20T08:45:00Z",
                "other_field": "value"
            },
            {
                "post_id": 4,
                "created_at": "2024-04-19T12:10:00Z",
                "other_field": "value"
            },
            {
                "post_id": 5,
                "created_at": "2024-04-18T09:20:00Z",
                "other_field": "value"
            },
            {
                "post_id": 6,
                "created_at": "2024-04-17T14:55:00Z",
                "other_field": "value"
            }
        ],
        2: [
            {
                "post_id": 7,
                "created_at": "2024-04-16T11:00:00Z",
                "other_field": "value"
            },
            {
                "post_id": 8,
                "created_at": "2024-04-15T10:30:00Z",
                "other_field": "value"
            },
            {
                "post_id": 9,
                "created_at": "2024-04-14T08:45:00Z",
                "other_field": "value"
            },
            {
                "post_id": 10,
                "created_at": "2024-04-13T12:10:00Z",
                "other_field": "value"
            },
            {
                "post_id": 11,
                "created_at": "2024-04-12T09:20:00Z",
                "other_field": "value"
            },
            {
                "post_id": 12,
                "created_at": "2024-04-11T14:55:00Z",
                "other_field": "value"
            }
        ]
    }
    post_comments = {
        1: [
            {
                "comment_id": 1,
                "created_at": "2024-04-22T11:20:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 2,
                "created_at": "2024-04-21T16:45:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 3,
                "created_at": "2024-04-20T09:30:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 4,
                "created_at": "2024-04-19T13:40:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 5,
                "created_at": "2024-04-18T10:55:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 6,
                "created_at": "2024-04-17T15:25:00Z",
                "other_field": "value"
            }
        ],
        2: [
            {
                "comment_id": 7,
                "created_at": "2024-04-16T14:20:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 8,
                "created_at": "2024-04-15T16:45:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 9,
                "created_at": "2024-04-14T12:30:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 10,
                "created_at": "2024-04-13T11:40:00Z",
                "other_field": "value"
            },
            {
                "comment_id": 11,
                "created_at": "2024-04-12T09:55:00Z",
                "other_field": "value"
            }
        ]
    }
    def get_user_comments(self, user_id):
        posts_by_user = self.send_request("user_post")
        comments_by_post = self.send_request("post_comment")
        posts = self.get_user_posts(user_id, posts_by_user)
        num_comments = 0
        for post in posts:
            num_comments += self.get_comments_numbers(post["post_id"], comments_by_post)
        return num_comments

    def send_request(self, endpoint):
        # res = request('GET', endpoint)
        if "user_post" in endpoint:
            return self.user_posts
        return self.post_comments

    def get_user_posts(self, user_id:int, posts_by_user: Dict[int, list]):
        return posts_by_user[user_id] if user_id in posts_by_user else []

    def get_comments_numbers(self, post_id, comments_by_post):
        return len(comments_by_post[post_id]) if post_id in comments_by_post else 0


if __name__ == '__main__':


    print(Solution().get_user_comments(1))