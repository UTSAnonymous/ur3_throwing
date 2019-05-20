classdef ur3_moveResponse < robotics.ros.Message
    %ur3_moveResponse MATLAB implementation of ur3_throwing/ur3_moveResponse
    %   This class was automatically generated by
    %   robotics.ros.msg.internal.gen.MessageClassGenerator.
    
    %   Copyright 2014-2019 The MathWorks, Inc.
    
    %#ok<*INUSD>
    
    properties (Constant)
        MessageType = 'ur3_throwing/ur3_moveResponse' % The ROS message type
    end
    
    properties (Constant, Hidden)
        MD5Checksum = '62ae02024e7918414d8b66756f34a1c6' % The MD5 Checksum of the message definition
    end
    
    properties (Access = protected)
        JavaMessage % The Java message object
    end
    
    properties (Dependent)
        Ack
    end
    
    properties (Constant, Hidden)
        PropertyList = {'Ack'} % List of non-constant message properties
        ROSPropertyList = {'Ack'} % List of non-constant ROS message properties
    end
    
    methods
        function obj = ur3_moveResponse(msg)
            %ur3_moveResponse Construct the message object ur3_moveResponse
            import com.mathworks.toolbox.robotics.ros.message.MessageInfo;
            
            % Support default constructor
            if nargin == 0
                obj.JavaMessage = obj.createNewJavaMessage;
                return;
            end
            
            % Construct appropriate empty array
            if isempty(msg)
                obj = obj.empty(0,1);
                return;
            end
            
            % Make scalar construction fast
            if isscalar(msg)
                % Check for correct input class
                if ~MessageInfo.compareTypes(msg(1), obj.MessageType)
                    error(message('robotics:ros:message:NoTypeMatch', obj.MessageType, ...
                        char(MessageInfo.getType(msg(1))) ));
                end
                obj.JavaMessage = msg(1);
                return;
            end
            
            % Check that this is a vector of scalar messages. Since this
            % is an object array, use arrayfun to verify.
            if ~all(arrayfun(@isscalar, msg))
                error(message('robotics:ros:message:MessageArraySizeError'));
            end
            
            % Check that all messages in the array have the correct type
            if ~all(arrayfun(@(x) MessageInfo.compareTypes(x, obj.MessageType), msg))
                error(message('robotics:ros:message:NoTypeMatchArray', obj.MessageType));
            end
            
            % Construct array of objects if necessary
            objType = class(obj);
            for i = 1:length(msg)
                obj(i,1) = feval(objType, msg(i)); %#ok<AGROW>
            end
        end
        
        function ack = get.Ack(obj)
            %get.Ack Get the value for property Ack
            ack = logical(obj.JavaMessage.getAck);
        end
        
        function set.Ack(obj, ack)
            %set.Ack Set the value for property Ack
            validateattributes(ack, {'logical', 'numeric'}, {'nonempty', 'scalar'}, 'ur3_moveResponse', 'Ack');
            
            obj.JavaMessage.setAck(ack);
        end
    end
    
    methods (Access = protected)
        function cpObj = copyElement(obj)
            %copyElement Implements deep copy behavior for message
            
            % Call default copy method for shallow copy
            cpObj = copyElement@robotics.ros.Message(obj);
            
            % Create a new Java message object
            cpObj.JavaMessage = obj.createNewJavaMessage;
            
            % Iterate over all primitive properties
            cpObj.Ack = obj.Ack;
        end
        
        function reload(obj, strObj)
            %reload Called by loadobj to assign properties
            obj.Ack = strObj.Ack;
        end
    end
    
    methods (Access = ?robotics.ros.Message)
        function strObj = saveobj(obj)
            %saveobj Implements saving of message to MAT file
            
            % Return an empty element if object array is empty
            if isempty(obj)
                strObj = struct.empty;
                return
            end
            
            strObj.Ack = obj.Ack;
        end
    end
    
    methods (Static, Access = {?matlab.unittest.TestCase, ?robotics.ros.Message})
        function obj = loadobj(strObj)
            %loadobj Implements loading of message from MAT file
            
            % Return an empty object array if the structure element is not defined
            if isempty(strObj)
                obj = robotics.ros.custom.msggen.ur3_throwing.ur3_moveResponse.empty(0,1);
                return
            end
            
            % Create an empty message object
            obj = robotics.ros.custom.msggen.ur3_throwing.ur3_moveResponse;
            obj.reload(strObj);
        end
    end
end