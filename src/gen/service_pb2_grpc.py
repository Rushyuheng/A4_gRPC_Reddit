# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import service_pb2 as service__pb2


class RedditStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/reddit.Reddit/CreatePost',
                request_serializer=service__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=service__pb2.CreatePostRespond.FromString,
                )
        self.VotePost = channel.unary_unary(
                '/reddit.Reddit/VotePost',
                request_serializer=service__pb2.VotePostRequest.SerializeToString,
                response_deserializer=service__pb2.VotePostRespond.FromString,
                )
        self.GetPost = channel.unary_unary(
                '/reddit.Reddit/GetPost',
                request_serializer=service__pb2.GetPostRequest.SerializeToString,
                response_deserializer=service__pb2.GetPostRespond.FromString,
                )
        self.CreateComment = channel.unary_unary(
                '/reddit.Reddit/CreateComment',
                request_serializer=service__pb2.CreateCommentRequest.SerializeToString,
                response_deserializer=service__pb2.CreateCommentRespond.FromString,
                )
        self.VoteComment = channel.unary_unary(
                '/reddit.Reddit/VoteComment',
                request_serializer=service__pb2.VoteCommentRequest.SerializeToString,
                response_deserializer=service__pb2.VoteCommentRespond.FromString,
                )
        self.GetMostUpvoteComment = channel.unary_stream(
                '/reddit.Reddit/GetMostUpvoteComment',
                request_serializer=service__pb2.MostUpvoteCommentRequest.SerializeToString,
                response_deserializer=service__pb2.MostUpvoteCommentRespond.FromString,
                )
        self.ExpandReply = channel.unary_stream(
                '/reddit.Reddit/ExpandReply',
                request_serializer=service__pb2.ExpandReplyRequest.SerializeToString,
                response_deserializer=service__pb2.ExpandReplyRespond.FromString,
                )


class RedditServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VotePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMostUpvoteComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExpandReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedditServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=service__pb2.CreatePostRequest.FromString,
                    response_serializer=service__pb2.CreatePostRespond.SerializeToString,
            ),
            'VotePost': grpc.unary_unary_rpc_method_handler(
                    servicer.VotePost,
                    request_deserializer=service__pb2.VotePostRequest.FromString,
                    response_serializer=service__pb2.VotePostRespond.SerializeToString,
            ),
            'GetPost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPost,
                    request_deserializer=service__pb2.GetPostRequest.FromString,
                    response_serializer=service__pb2.GetPostRespond.SerializeToString,
            ),
            'CreateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComment,
                    request_deserializer=service__pb2.CreateCommentRequest.FromString,
                    response_serializer=service__pb2.CreateCommentRespond.SerializeToString,
            ),
            'VoteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteComment,
                    request_deserializer=service__pb2.VoteCommentRequest.FromString,
                    response_serializer=service__pb2.VoteCommentRespond.SerializeToString,
            ),
            'GetMostUpvoteComment': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMostUpvoteComment,
                    request_deserializer=service__pb2.MostUpvoteCommentRequest.FromString,
                    response_serializer=service__pb2.MostUpvoteCommentRespond.SerializeToString,
            ),
            'ExpandReply': grpc.unary_stream_rpc_method_handler(
                    servicer.ExpandReply,
                    request_deserializer=service__pb2.ExpandReplyRequest.FromString,
                    response_serializer=service__pb2.ExpandReplyRespond.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reddit.Reddit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Reddit(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.Reddit/CreatePost',
            service__pb2.CreatePostRequest.SerializeToString,
            service__pb2.CreatePostRespond.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VotePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.Reddit/VotePost',
            service__pb2.VotePostRequest.SerializeToString,
            service__pb2.VotePostRespond.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.Reddit/GetPost',
            service__pb2.GetPostRequest.SerializeToString,
            service__pb2.GetPostRespond.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.Reddit/CreateComment',
            service__pb2.CreateCommentRequest.SerializeToString,
            service__pb2.CreateCommentRespond.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.Reddit/VoteComment',
            service__pb2.VoteCommentRequest.SerializeToString,
            service__pb2.VoteCommentRespond.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMostUpvoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/reddit.Reddit/GetMostUpvoteComment',
            service__pb2.MostUpvoteCommentRequest.SerializeToString,
            service__pb2.MostUpvoteCommentRespond.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExpandReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/reddit.Reddit/ExpandReply',
            service__pb2.ExpandReplyRequest.SerializeToString,
            service__pb2.ExpandReplyRespond.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
