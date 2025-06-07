import React from 'react';
import styled from 'styled-components';

const GreetingWrapper = styled.div`
  padding: 20px;
  background-color: #f0f8ff;
  border: 1px solid #b0c4de;
  border-radius: 8px;
  text-align: center;
  font-size: 1.2rem;
`;

const Greeting: React.FC = () => {
  return (
    <GreetingWrapper>
      Hello from your new component!
    </GreetingWrapper>
  );
};

export default Greeting;
