# SupportText

元のフォルダ: `src/components/SupportText/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: SupportText.tsx -->
````tsx
import type { ComponentProps } from 'react';

export type SupportTextProps = ComponentProps<'p'>;

export const SupportText = (props: SupportTextProps) => {
  const { children, className, ...rest } = props;

  return (
    <p className={`text-std-16N-170 text-solid-gray-600 ${className ?? ''}`} {...rest}>
      {children}
    </p>
  );
};
````

<!-- file: index.ts -->
````ts
export { SupportText } from './SupportText';
````
